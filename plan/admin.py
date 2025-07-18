from django.contrib import admin

from plan.models import PlanModel


@admin.register(PlanModel)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('order', 'plan_date', 'pre_plan_date')
    list_filter = ('plan_date', 'pre_plan_date')
    search_fields = ('order',)
    ordering = ['order',]
    list_editable = ('plan_date', 'pre_plan_date')