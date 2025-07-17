from django.db import models

from office.models.order_model import OrderModel

class EtapModel(models.Model):
    
    title = models.CharField(max_length=100)
    product = models.ForeignKey('company.ProductModel', on_delete=models.PROTECT, verbose_name='Продукт')
    subsequence = models.IntegerField(default=0, verbose_name='Порядковый номер')
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'etap'
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'
        ordering = ['title', 'product', 'subsequence']

class OrderEtapModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.PROTECT, verbose_name='Заказ')
    etap = models.ForeignKey(EtapModel, on_delete=models.PROTECT, verbose_name='Этап')
    date = models.DateField(verbose_name='Дата', null=True, blank=True)
    status = models.CharField(max_length=16, verbose_name='Статус', choices=[
        ('NEW', 'Новый'),
        ('IN_WORK', 'В работе'),
        ('DONE', 'Выполнен'),
        ('CANCELED', 'Отменен'),
    ])
    responsible = models.ForeignKey('employees.EmployeeModel', on_delete=models.PROTECT, verbose_name='Ответственный', null=True, blank=True)

    class Meta:
        db_table = 'order_etap'
        verbose_name = 'Этап заказа'
        verbose_name_plural = 'Этапы заказа'
        ordering = ['order', 'etap']
