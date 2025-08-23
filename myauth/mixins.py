from django.core.exceptions import PermissionDenied
from employees.models import EmployeeModel

class PermissionsByUserMixin:

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