from django.contrib import admin
from .models.bots import Bots, TokensTelegram, TokensViber, TokensFacebook


class BotsAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'type_messenger', 'created_date']
    search_fields = ['name', 'type_messenger']


class TokensTelegramAdmin(admin.ModelAdmin):
    list_display = ['bot', 'token', 'created_date']


class TokensViberAdmin(admin.ModelAdmin):
    list_display = ['bot', 'token', 'created_date']


class TokensFacebookAdmin(admin.ModelAdmin):
    list_display = ['bot', 'token', 'verify_token', 'id_page', 'created_date']


admin.site.register(Bots, BotsAdmin)
admin.site.register(TokensTelegram, TokensTelegramAdmin)
admin.site.register(TokensViber, TokensViberAdmin)
admin.site.register(TokensFacebook, TokensFacebookAdmin)
