from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from employees.models import EmployeeModel

class PermissionRequiredMixin:
    """Миксин для проверки разрешений через должность сотрудника"""
    permission_required = None
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        # Проверяем разрешение
        if self.permission_required and not self.has_permission(request.user):
            raise PermissionDenied("У вас нет прав для этого действия")
        
        return super().dispatch(request, *args, **kwargs)
    
    def has_permission(self, user):
        """Проверяет, есть ли у пользователя нужное разрешение через его должность"""
        try:
            # Получаем сотрудника связанного с пользователем
            employee = user.employee
            
            # Проверяем, есть ли у должности сотрудника нужное разрешение
            return employee.role.permissions.filter(
                permission__code_name=self.permission_required
            ).exists()
            
        except (EmployeeModel.DoesNotExist, AttributeError):
            return False

class RoleRequiredMixin:
    """Миксин для проверки конкретной должности"""
    role_required = None  # Название должности
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if self.role_required and not self.has_role(request.user):
            raise PermissionDenied("У вас нет нужной должности для этого действия")
        
        return super().dispatch(request, *args, **kwargs)
    
    def has_role(self, user):
        """Проверяет, есть ли у пользователя нужная должность"""
        try:
            employee = user.employee
            return employee.role.title == self.role_required
        except (EmployeeModel.DoesNotExist, AttributeError):
            return False