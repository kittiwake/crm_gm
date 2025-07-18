from django.db import models
# from django.contrib.auth.models import User
from datetime import date, timedelta

class LeadModel(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', 'Новый'
        IN_WORK = 'IN_WORK', 'В обработке'
        CONTRACT = 'CONTRACT', 'Заключен'
        CANCELED = 'CANCELED', 'Отменен'
        WAIT = 'WAIT', 'В ожидании'

    contract = models.CharField(max_length=16, unique=True, db_index=True, verbose_name='Номер заказа')
    contact_date = models.DateField(verbose_name='Дата добавления', null=False, blank=False)
    name = models.CharField(max_length=64, verbose_name='ФИО', null=False, blank=False)
    product = models.CharField(max_length=30, verbose_name='Наименование')
    adress = models.CharField(max_length=128, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    email = models.CharField(max_length=30, verbose_name='E-mail')

    note = models.CharField(max_length=512, verbose_name='Примечание', null=True, blank=True)
    status = models.CharField(max_length=16, verbose_name='Статус', choices=Status.choices, default=Status.NEW)
    manager = models.ForeignKey('employees.EmployeeModel', on_delete=models.PROTECT, verbose_name='Менеджер', null=True, blank=True)

    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'
        ordering = ['contract']

    def __str__(self):
        return self.contract