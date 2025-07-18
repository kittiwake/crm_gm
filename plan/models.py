from django.db import models

class PlanModel(models.Model):

    order = models.OneToOneField('office.OrderModel', on_delete=models.CASCADE, verbose_name='Заказ')
    plan_date = models.DateField(verbose_name='Планируемая дата', null=True, blank=True)
    pre_plan_date = models.DateField(verbose_name='Предварительная дата', null=True, blank=True)

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'
        ordering = ['-plan_date']
