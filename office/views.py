from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from django.views import View

from plan.models import PlanModel
from .models.order_model import OrderModel


class Timetable(View):
    template_name = 'timetable.html'

    def get(self, request):
        # Рассчитываем период
        today = timezone.now().date()
        start_date = today - timedelta(weeks=2)
        end_date = today + timedelta(weeks=6)
        
        # Получаем заказы за период
        orders = OrderModel.objects.select_related('planmodel').filter(
            planmodel__plan_date__gte=start_date,
            planmodel__plan_date__lte=end_date
        ).order_by('term')
        
        waiting_orders = PlanModel.objects.filter(
            plan_date__isnull=True,
        ).order_by('order')
        print(waiting_orders)
        orders_without_plan = OrderModel.objects.filter(planmodel__isnull=True)

        # Создаем структуру календаря
        calendar_weeks = []
        current_date = start_date
        
        # Выравниваем начальную дату на понедельник
        while current_date.weekday() != 0:  # 0 - понедельник
            current_date -= timedelta(days=1)
        
        # Формируем недели
        while current_date <= end_date:
            week = []
            for day_num in range(5):  # Только пн-пт
                day_date = current_date + timedelta(days=day_num)
                day_orders = [o for o in orders if o.planmodel.plan_date == day_date]
                week.append({
                    'date': day_date,
                    'orders': day_orders,
                    'is_today': day_date == today
                })
            calendar_weeks.append(week)
            current_date += timedelta(weeks=1)
        
        context = {
            'weeks': calendar_weeks,
            'period_start': start_date,
            'period_end': end_date,
            'waiting_orders': waiting_orders,
            'orders_without_plan': orders_without_plan
        }
        
        return render(request, self.template_name, context)
    

class Order(View):
    template_name = 'order.html'

    def get(self, request, id):
        order = OrderModel.objects.get(id=id)
        context = {
            'order': order
        }

        return render(request, self.template_name, context)