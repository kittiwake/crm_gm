# employees/models.py
from django.db import models
from django.contrib.auth.models import User

class RoleModel(models.Model):
    
    title = models.CharField(verbose_name="Должность", max_length=50)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = ["title"]

    def __str__(self):
        return self.title
    
class EmployeeModel(models.Model):

    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    role = models.ForeignKey(RoleModel, on_delete=models.PROTECT, verbose_name="Должность", related_name='employees',)
    email = models.EmailField(verbose_name="E-mail", blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=20, blank=True)
    tg_nickname = models.CharField(max_length=50,null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Работает ли в компании", default=True)
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE, 
        verbose_name="Профиль пользователя",
        null=True,
        blank=True
)
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role.title if self.role else 'нет должности'})"
    
class FreemenModel(models.Model):

    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, verbose_name="Сотрудник", related_name='freemen')
    begin_date = models.DateField(verbose_name="Первый день", null=False, blank=False)
    end_date = models.DateField(verbose_name="Последний день", null=False, blank=False)

    class Meta:
        verbose_name = "Отпуск"
        verbose_name_plural = "Отпуски"
        ordering = ["begin_date", "end_date"]

    def __str__(self):
        return f"{self.employee.last_name} {self.employee.first_name} ({self.begin_date} - {self.end_date})"
