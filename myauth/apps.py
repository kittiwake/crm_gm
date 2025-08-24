from django.apps import AppConfig


class MyauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myauth'

    def ready(self):
        # Этот код выполнится ОДИН РАЗ при запуске Django
        from django.contrib.auth.models import User
        from .utils import check_custom_permission
        
        # Добавляем метод ко всем пользователям
        User.add_to_class('has_custom_permission', lambda self, code: check_custom_permission(self, code))
        