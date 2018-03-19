from django.contrib import admin
from users.models.profiles import Profiles


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['user', 'hash', 'role', 'created_date']


admin.site.register(Profiles, ProfilesAdmin)
