from django.contrib import admin

from accounts.models import UserProfileModel

@admin.register(UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'tg_nickname')
    search_fields = ('user', 'phone', 'tg_nickname')
    ordering = ('user',)
    
