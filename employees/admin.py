from django.contrib import admin
from .models import RoleModel, EmployeeModel

@admin.register(RoleModel)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'role', 'is_active', 'user')
    list_filter = ('role', 'is_active')
    search_fields = ('last_name', 'first_name', 'email')
    list_editable = ('is_active',)
    ordering = ('last_name', 'first_name', 'role')