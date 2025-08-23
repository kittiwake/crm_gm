from django.contrib import admin
from .models import PermissionModel, RolePermissionModel

@admin.register(PermissionModel)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'code_name', 'description']
    list_filter = ['code_name']
    search_fields = ['name', 'code_name']
    ordering = ['name']

@admin.register(RolePermissionModel)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ['role', 'permission']
    list_filter = ['role', 'permission']
    search_fields = ['role__title', 'permission__name']
    ordering = ['role__title']