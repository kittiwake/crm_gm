from django.contrib import admin

from .models.lead_model import LeadModel
from .models.order_model import OrderModel

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('contract', 'company', 'term', 'sum', 'prepayment', 'rassr', 'beznal', 'rebate')
    list_filter = ('company', 'rassr', 'beznal')
    search_fields = ('contract',)
    ordering = ['term', 'contract']
    list_editable = ('rassr', 'beznal')

@admin.register(LeadModel)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('contract', 'name', 'phone', 'email', 'status')
    search_fields = ('contract', 'name', 'phone', 'email')
    ordering = ['contract', 'name']
    list_filter = ('status',)
    list_editable = ('status',)