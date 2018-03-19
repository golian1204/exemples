import coreapi

from functools import wraps
from django.conf import settings
from api_service import celery_app
from mess.models.mess import MessStatus
from datetime import datetime


def auth(func):
    """Декоратор для авторизации, декорируемая функция первым аргументом принимает токен"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        credentials = {
            'username': settings.API_MESSENGER_AUTH_LOGIN,
            'password': settings.API_MESSENGER_AUTH_PASSWORD,
        }
        client = coreapi.Client()
        schema = client.get(settings.API_MESSENGER_BASE_URL)
        result = client.action(schema, ['auth', 'create'], credentials)

        auth = coreapi.auth.TokenAuthentication(
            scheme='Token',
            token=result['data']['token']
        )
        client = coreapi.Client(auth=auth)

        result = func(client, *args, **kwargs)

        return result
    return wrapper


@celery_app.task
@auth
def send_message_to_api_message(client, data):
    """Отправка сообщений на API_MESSAGES"""
    message = MessStatus.objects.get(id=data.get('message_id'))

    message.process_status = message.QUEUE
    message.save()

    schema = client.get(settings.API_MESSENGER_BASE_URL)
    response = client.action(schema, ['sendmessage', 'create'], params=data)

    if response.get('status') == 'success':
        message.process_status = message.SENT_TO_API_MESSAGE
        message.send_date = datetime.now()
        message.save()


@celery_app.task
def send_deferred_message():
    def to_task_api_messages(message):
        data = {
            'mess': {
                'text': message.mess.text,
            },
            'subscriber': {
                'bot_id': message.subscriber.bot_id,
                'name_messenger': message.subscriber.name_messenger,
            },
            'user_id': message.mess.user.id,
            'message_id': message.id,
        }
        send_message_to_api_message.delay(data=data)

    messages = MessStatus.objects.filter(
        process_status=MessStatus.CREATE, plan_send_date__lte=datetime.now()
    ).select_related('mess', 'subscriber')

    list(map(to_task_api_messages, messages))
