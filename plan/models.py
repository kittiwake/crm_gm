from django.db import models

class PlanModel(models.Model):

    order = models.OneToOneField('office.OrderModel', on_delete=models.CASCADE, verbose_name='Заказ')
    plan_date = models.DateField(verbose_name='Планируемая дата', null=True, blank=True)
    pre_plan_date = models.DateField(verbose_name='Предварительная дата', null=True, blank=True)

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'
        ordering = ['-plan_date']

class PlanTechModel(models.Model):
    order = models.ForeignKey('office.OrderModel', on_delete=models.PROTECT, verbose_name='Заказ')
    employee = models.ForeignKey('employees.EmployeeModel', on_delete=models.PROTECT, verbose_name='конструктор')
    date = models.DateField(verbose_name='Дата')
    status = models.CharField(max_length=16, verbose_name='Статус', choices=[
        ('NEW', 'Новый'),
        ('IN_WORK', 'В работе'),
        ('DONE', 'Выполнен'),
        ('CANCELED', 'Отменен'),
    ])

    class Meta:
        verbose_name = 'План конструктора'
        verbose_name_plural = 'Планы конструктора'
        ordering = ['-date']
