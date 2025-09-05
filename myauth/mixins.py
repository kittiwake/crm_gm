from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth.views import redirect_to_login

class PermissionsByUserMixin:
    """Миксин для проверки разрешений через должность сотрудника"""
    permission_required = None
    login_url = '/auth/login/'  # Укажите ваш URL для входа
    permission_denied_message = "У вас нет прав для этого действия"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
       
        # Проверяем разрешение
        if self.permission_required and not request.user.has_custom_permission(self.permission_required):
            return self.handle_permission_denied()
        
        return super().dispatch(request, *args, **kwargs)
    
    def handle_no_permission(self):
        """Обработка неавторизованного пользователя"""
        return redirect_to_login(
            self.request.get_full_path(), 
            self.login_url
        )
    
    def handle_permission_denied(self):
        """Обработка отсутствия прав у авторизованного пользователя"""
        raise PermissionDenied(self.permission_denied_message)