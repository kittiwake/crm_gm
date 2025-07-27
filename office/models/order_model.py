from django.db import models
# from django.contrib.auth.models import User
from datetime import date, timedelta


class OrderModel(models.Model):

    contract = models.CharField(
        max_length=16,
        db_index=True,
        unique=True,
        verbose_name='Номер заказа',
        blank=False,
        null=True,
    )    
    lead = models.ForeignKey(
        'LeadModel', 
        on_delete=models.PROTECT, 
        verbose_name='Лид',
        null=True,  # Разрешаем NULL для заказов без лида
        blank=True
    )   
    client_name = models.CharField(
        max_length=64, 
        verbose_name='Имя заказчика', 
        null=True, blank=True
        ) 
    delivery_address = models.CharField(max_length=128, verbose_name='Адрес доставки', default='', blank=True)
    contract_date = models.DateField(verbose_name='Дата заключения', null=False, blank=False)
    company = models.ForeignKey('company.CompanyModel', on_delete=models.PROTECT, verbose_name='Компания', default=1)
    product = models.CharField(max_length=30, verbose_name='Наименование')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    email = models.CharField(max_length=30, verbose_name='E-mail', null=True, blank=True)
    personal_agree = models.CharField(verbose_name='Согласие на обработку персональных данных', max_length=8, choices=[
        ('disagree', 'Не согласен'),
        ('agree', 'Согласен'),
    ], default='disagree')
    add_date = models.DateField(verbose_name='Дата внесения', null=False, blank=False, default=date.today())
    term = models.DateField(verbose_name='Срок', null=False, blank=False, default=date.today() + timedelta(weeks=4))
    sum = models.DecimalField(verbose_name='Сумма договора', max_digits=16, decimal_places=2, default=0)
    prepayment = models.DecimalField(verbose_name='Предоплата', max_digits=16, decimal_places=2, default=0)
    rassr = models.BooleanField(verbose_name='Рассрочка', default=False)
    beznal = models.BooleanField(verbose_name='Безнал', default=False)
    rebate = models.IntegerField(verbose_name='Комиссия', default=0)
    note = models.CharField(max_length=512, verbose_name='Примечание', null=True, blank=True)
    attention = models.IntegerField(default=0, verbose_name='Внимание')
    sumdeliv = models.IntegerField(verbose_name='Сумма доставки', default=0)
    sumcollect = models.IntegerField(verbose_name='Сумма сборки', default=0)
    archive = models.BooleanField(verbose_name='Удален', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['lead']

    def __str__(self):
        return self.lead.contract
    