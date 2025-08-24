from functools import wraps
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

def role_permission_required(permission_code):
    """
    Кастомный декоратор для проверки прав вашей системы
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return JsonResponse({"error": "Требуется авторизация"}, status=401)
            
            # Используем вашу систему прав
            if not request.user.has_custom_permission(permission_code):
                raise PermissionDenied(f"Требуется разрешение: {permission_code}")
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator