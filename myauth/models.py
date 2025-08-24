from django.db import models
from django.contrib.auth.models import User
from employees.models import RoleModel  # импортируем из вашего приложения
from .permissions import PERMISSIONS


class RolePermissionModel(models.Model):
    """Связь ролей и разрешений"""
    role = models.ForeignKey(
        RoleModel, 
        on_delete=models.CASCADE, 
        verbose_name="Должность",
        related_name='permissions'
    )
    permission = models.CharField(
        max_length=50,
        choices=PERMISSIONS.CHOICES,
        verbose_name="Разрешение"
    )
    
    class Meta:
        verbose_name = "Разрешение должности"
        verbose_name_plural = "Разрешения должностей"
        unique_together = ['role', 'permission']
    
    def __str__(self):
        return f"{self.role.title} - {self.permission_name}"
    
    @property
    def permission_name(self):
        """Возвращает человекочитаемое название разрешения"""
        return dict(PERMISSIONS.CHOICES).get(self.permission, self.permission)
    