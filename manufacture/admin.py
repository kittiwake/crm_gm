from django.contrib import admin

from manufacture.models import EtapModel, OrderEtapModel

@admin.register(EtapModel)
class EtapModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'subsequence')
    ordering = ['subsequence', 'product', 'title']
    list_editable = ('subsequence',)


@admin.register(OrderEtapModel)
class OrderEtapModelAdmin(admin.ModelAdmin):
    list_display = ('order', 'etap', 'status', 'date', 'responsible')
    ordering = ['order', 'etap', 'date']
    list_filter = ('status', 'etap', 'date')
    list_editable = ('status',)