from django.contrib import admin
from .models import PermissionModel, RolePermissionModel


class RoleInline(admin.TabularInline):
    """Inline для разрешений роли"""
    model = RolePermissionModel
    extra = 1  # Количество пустых форм
    verbose_name = "Должность"
    verbose_name_plural = "Должности"
    autocomplete_fields = ['role']  # Автодополнение для разрешений

@admin.register(PermissionModel)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'code_name', 'description']
    list_filter = ['code_name']
    search_fields = ['name', 'code_name']
    ordering = ['name']
    inlines = [RoleInline]

@admin.register(RolePermissionModel)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ['role', 'permission']
    list_filter = ['role', 'permission']
    search_fields = ['role__title', 'permission__name']
    ordering = ['role__title']