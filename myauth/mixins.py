from django.core.exceptions import PermissionDenied

class PermissionsByUserMixin:

    """Миксин для проверки разрешений через должность сотрудника"""
    permission_required = None
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        # Проверяем разрешение
        if self.permission_required and not request.user.has_custom_permission(self.permission_required):
            raise PermissionDenied("У вас нет прав для этого действия")
        
        return super().dispatch(request, *args, **kwargs)
    