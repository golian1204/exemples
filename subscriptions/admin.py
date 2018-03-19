from django.contrib import admin
from subscriptions.models.subscribers import Subscribers, Subscriptions
from subscriptions.models.subs_list import SubsList
from subscriptions.models.subs_blank import SubsBlank


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['user', 'bot_id', 'name_messenger', 'username', 'first_name', 'last_name', 'created_date', 'subscribed', 'chat_bot', 'phone']


admin.site.register(Subscribers, SubscribersAdmin)


class SubsListAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'user', 'uuid', 'created_date', 'deleted']


admin.site.register(SubsList, SubsListAdmin)


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ['subs_list', 'subscriber', 'created_date', 'deleted']


admin.site.register(Subscriptions, SubscriptionsAdmin)


class SubsBlankAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'offer', 'call_to_action', 'telegram', 'facebook', 'viber', 'subs_list',
                    'image', 'phone', 'timer_date', 'local_time', 'timer_interval', 'right_now', 'utp', 'cta',
                    'confidentiality', 'user', 'created_date', 'deleted']


admin.site.register(SubsBlank, SubsBlankAdmin)
