from django.contrib import admin
from .models import RolePermissionModel


class RoleInline(admin.TabularInline):
    """Inline для разрешений роли"""
    model = RolePermissionModel
    extra = 1  # Количество пустых форм
    verbose_name = "Должность"
    verbose_name_plural = "Должности"
    autocomplete_fields = ['role']  # Автодополнение для разрешений


@admin.register(RolePermissionModel)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ['role', 'permission_name']
    list_filter = ['role', 'permission']
    search_fields = ['role__title', 'permission__name']
    ordering = ['role__title', 'permission']
    
    def permission_name(self, obj):
        return obj.permission_name
    permission_name.short_description = 'Название разрешения'