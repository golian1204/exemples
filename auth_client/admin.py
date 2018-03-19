from django.contrib import admin
from auth_client.models.messengers import Messengers


class MessengersAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_id_bot', 'name_messenger', 'bot_id', 'created_date']


admin.site.register(Messengers, MessengersAdmin)
