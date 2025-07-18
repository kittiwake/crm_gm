import json
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta

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

    def post(self, request):
        print(request.path)
        if 'set-plan-date' in request.path:
            # Обработка установки даты
            print('идем менять дату')
            return self.handle_set_plan_date(request)
        
        return JsonResponse({"error": "Unknown action"}, status=400)

    def handle_set_plan_date(self, request):
        try:
            data = json.loads(request.body)
            print(data)
            order_id = data.get('order_id')
            plan_date = data.get('plan_date')
            plan_date = datetime.strptime(plan_date, '%Y-%m-%d').date()
            if not order_id or not plan_date:
                return JsonResponse({"error": "Missing order_id or plan_date"}, status=400)

            # Одной операцией обновляем или создаем запись
            order, created = PlanModel.objects.update_or_create(
                order_id=order_id,  # Используем order_id вместо order__id
                defaults={
                    'plan_date': plan_date
                }
            )
            
            return JsonResponse({
                "success": True,
                "formatted_date": order.plan_date.strftime('%d.%m.%Y'),
                "created": created  # Дополнительно возвращаем флаг создания
            }, status=200)
            
        except OrderModel.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)