from django.contrib import admin
from mess.models import attachments, buttons, dialogs, feedback, mess, polls, statistics, smart


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['link', 'name', 'weight', 'created_date', 'order']


class VideosAdmin(admin.ModelAdmin):
    list_display = ['link', 'name', 'weight', 'created_date', 'order']


class AudiosAdmin(admin.ModelAdmin):
    list_display = ['link', 'name', 'weight', 'created_date', 'order']


class FilesAdmin(admin.ModelAdmin):
    list_display = ['link', 'name', 'weight', 'created_date', 'order']


class AnswersAdmin(admin.ModelAdmin):
    list_display = ['interview', 'title', 'order']


class InterviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_date']


class ValuationAdmin(admin.ModelAdmin):
    list_display = ['scale', 'icon']


class LinkButtonAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['title']


class MessAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'images', 'videos', 'audios', 'files', 'interview', 'valuation', 'yesno', 'like', 'invite', 'telegram', 'facebook', 'viber',
                    'link_button', 'payment', 'created_date', 'user', 'draft', 'time_before', 'time_after', 'subs_online', 'deleted']


class MessStatusAdmin(admin.ModelAdmin):
    list_display = ['mess', 'subscriber', 'plan_send_date', 'create_date', 'send_date', 'delivery_date', 'read_date', 'action_date', 'process_status']


class DialogsAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscriber']


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['dialog', 'user_sender', 'text', 'mess', 'send_date']


class AutoAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'key_word', 'anti_word', 'mess', 'create_date']


class YesNoAnswerAdmin(admin.ModelAdmin):
    list_display = ['mess', 'yes', 'no']


class YesNoStatisticsAdmin(admin.ModelAdmin):
    list_display = ['mess', 'subscriber', 'yes']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price']


admin.site.register(attachments.Images, ImagesAdmin)
admin.site.register(attachments.Videos, VideosAdmin)
admin.site.register(attachments.Audios, AudiosAdmin)
admin.site.register(attachments.Files, FilesAdmin)
admin.site.register(polls.Answers, AnswersAdmin)
admin.site.register(polls.Interview, InterviewAdmin)
admin.site.register(feedback.Valuation, ValuationAdmin)
admin.site.register(buttons.LinkButton, LinkButtonAdmin)
admin.site.register(buttons.Payment, PaymentAdmin)
admin.site.register(mess.Mess, MessAdmin)
admin.site.register(mess.MessStatus, MessStatusAdmin)
admin.site.register(dialogs.Dialogs, DialogsAdmin)
admin.site.register(dialogs.Messages, MessagesAdmin)
admin.site.register(dialogs.AutoAnswer, AutoAnswerAdmin)
admin.site.register(dialogs.YesNoAnswer, YesNoAnswerAdmin)
admin.site.register(statistics.YesNoStatistic, YesNoStatisticsAdmin)
admin.site.register(smart.Category, CategoryAdmin)
admin.site.register(smart.Product, ProductAdmin)
