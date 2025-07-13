from django.db import models
class ProductModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']

class CompanyModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    product = models.ForeignKey('ProductModel', on_delete=models.PROTECT, verbose_name='Продукт')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'company'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['title']