from django.core.cache import cache
from .permissions import PERMISSIONS

def check_custom_permission(user, permission_code):
    """
    Основная логика проверки прав
    """
    if not user or not user.is_authenticated:
        return False
    if permission_code not in PERMISSIONS.DICT:
        return False
    
    cache_key = f"user_{user.id}_perm_{permission_code}"
    has_perm = cache.get(cache_key)
    
    if has_perm is None:
        try:
            employee = user.employee
            has_perm = employee.role.permissions.filter(
                permission=permission_code
            ).exists()
            cache.set(cache_key, has_perm, timeout=3000)
        except Exception:
            has_perm = False
            cache.set(cache_key, has_perm, timeout=60)
    
    return has_perm
