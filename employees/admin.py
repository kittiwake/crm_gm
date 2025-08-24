from django.contrib import admin
from .models import RoleModel, EmployeeModel
from myauth.models import RolePermissionModel  # импортируем из myauth

class PermissionInline(admin.TabularInline):
    """Inline для разрешений роли"""
    model = RolePermissionModel
    extra = 1  # Количество пустых форм
    verbose_name = "Разрешение"
    verbose_name_plural = "Разрешения"
    fields = ['permission']  # Автодополнение для разрешений

@admin.register(RoleModel)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'permissions_count')
    search_fields = ('title',)
    ordering = ('title',)
    inlines = [PermissionInline]  # Добавляем inline
    
    def permissions_count(self, obj):
        """Отображает количество разрешений у роли"""
        return obj.permissions.count()
    permissions_count.short_description = 'Количество разрешений'

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'role', 'is_active', 'user')
    list_filter = ('role', 'is_active')
    search_fields = ('last_name', 'first_name', 'email')
    list_editable = ('is_active',)
    ordering = ('last_name', 'first_name', 'role')