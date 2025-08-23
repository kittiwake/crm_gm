from django.db import models
from django.contrib.auth.models import User
from employees.models import RoleModel  # импортируем из вашего приложения

class PermissionModel(models.Model):
    """Модель для разрешений"""
    name = models.CharField(max_length=100, verbose_name="Название разрешения")
    code_name = models.CharField(max_length=100, unique=True, verbose_name="Кодовое имя")
    description = models.TextField(blank=True, verbose_name="Описание")
    
    class Meta:
        verbose_name = "Разрешение"
        verbose_name_plural = "Разрешения"
        ordering = ["name"]
    
    def __str__(self):
        return self.name

class RolePermissionModel(models.Model):
    """Связь ролей и разрешений"""
    role = models.ForeignKey(
        RoleModel, 
        on_delete=models.CASCADE, 
        verbose_name="Должность",
        related_name='permissions'
    )
    permission = models.ForeignKey(
        PermissionModel, 
        on_delete=models.CASCADE, 
        verbose_name="Разрешение"
    )
    
    class Meta:
        verbose_name = "Разрешение должности"
        verbose_name_plural = "Разрешения должностей"
        unique_together = ['role', 'permission']
    
    def __str__(self):
        return f"{self.role.title} - {self.permission.name}"