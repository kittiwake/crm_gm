from django.contrib import admin

from .models import CompanyModel, ProductModel

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)   

@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    ordering = ('title',)