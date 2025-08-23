import json
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime, timedelta
from django.db import transaction
from django.contrib import messages
from django.views import View

from employees.models import EmployeeModel
from myauth.mixins import PermissionsByUserMixin
from office.forms import LeadForm, OrderForm
from office.models.lead_model import LeadModel
from plan.models import PlanModel
from office.models.order_model import OrderModel

class Timetable(PermissionsByUserMixin, View):
    template_name = 'timetable.html'
    permission_required = 'view_timetable'


    def get(self, request):
        print(request.user.employee.role, '----------- user')
        # Рассчитываем период
        today = timezone.now().date()
        start_date = today - timedelta(weeks=2)
        end_date = today + timedelta(weeks=6)
        
        # Получаем заказы за период
        orders = OrderModel.objects.select_related('lead').select_related('planmodel').filter(
            planmodel__plan_date__gte=start_date,
            planmodel__plan_date__lte=end_date
        ).order_by('term')
        
        waiting_orders = PlanModel.objects.select_related('order').filter(
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
    

class Order(PermissionsByUserMixin, View):
    template_name = 'order.html'
    permission_required = 'view_order'

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
        
from django.views.generic.edit import CreateView

class CreateLead(CreateView):
    model = LeadModel
    form_class = LeadForm
    template_name = 'add_lead.html'
    success_url = reverse_lazy('office:kanban')

    def form_valid(self, form):
        # Устанавливаем текущую дату перед сохранением
        form.instance.contact_date = timezone.now().date()
        form.instance.phone = '+7' + form.instance.phone
        return super().form_valid(form)


class CreateOrder(CreateView):
    model = OrderModel
    form_class = OrderForm
    template_name = 'add_order.html'
    success_url = reverse_lazy('create_order')


    def get_context_data(self, **kwargs):
        """Добавляем список лидов в контекст шаблона"""
        context = super().get_context_data(**kwargs)
        context['completed_leads'] = LeadModel.objects.filter(status=LeadModel.Status.CONTRACT)
        print(context['completed_leads'])
        return context
    
    def get_initial(self):
        """Устанавливаем начальные значения для формы"""
        initial = super().get_initial()
        if 'lead_id' in self.kwargs:
            lead = get_object_or_404(LeadModel, pk=self.kwargs['lead_id'])
            initial.update({
                'contract': lead.contract,
                'product': lead.product,
                'phone': lead.phone,
                'email': lead.email,
                'lead': lead.id
            })
        return initial
    
    def get_form_kwargs(self):
        """Добавляем lead_id в аргументы формы"""
        kwargs = super().get_form_kwargs()
        if 'lead_id' in self.kwargs:
            kwargs['lead_id'] = self.kwargs['lead_id']
        return kwargs
    
    def form_valid(self, form):
        """Дополнительная обработка перед сохранением"""
        print("Form is valid:", form.is_valid())  # Проверка валидности
        print("Form errors:", form.errors)
        try:
            with transaction.atomic():
                if 'lead_id' in self.kwargs:
                    lead = get_object_or_404(LeadModel, pk=self.kwargs['lead_id'])
                    form.instance.add_date = timezone.now().date()
                    form.instance.personal_agree = False
                    form.instance.lead = lead
                    response = super().form_valid(form)
                    lead.status = LeadModel.Status.DONE
                    lead.save()
                    return response
                return super().form_valid(form)
        except Exception as e:
            print("Error:", e)
            return self.form_invalid(form)


# leads/views.py
from django.views.generic import TemplateView
from employees.models import EmployeeModel

class KanbanBoardView(TemplateView):
    template_name = 'kanban.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Получаем все лиды с менеджерами
        leads = LeadModel.objects.select_related('manager')
        
        # Группируем лиды по статусам
        status_groups = {
            'NEW': {
                'leads': leads.filter(status='NEW'),
                'title': 'Новый',
                'color': 'danger',
                'icon': 'fa-plus-circle'
            },
            'IN_WORK': {
                'leads': leads.filter(status='IN_WORK'),
                'title': 'В обработке',
                'color': 'warning',
                'icon': 'fa-spinner'
            },
            'WAIT': {
                'leads': leads.filter(status='WAIT'),
                'title': 'В ожидании',
                'color': 'info',
                'icon': 'fa-clock'
            },
            'CONTRACT': {
                'leads': leads.filter(status='CONTRACT'),
                'title': 'Заключен',
                'color': 'success',
                'icon': 'fa-check-circle'
            },
            'DONE': {
                'leads': leads.filter(status='DONE'),
                'title': 'Выполнен',
                'color': 'success',
                'icon': 'fa-flag-checkered'
            },
            'CANCELED': {
                'leads': leads.filter(status='CANCELED'),
                'title': 'Отменен',
                'color': 'danger',
                'icon': 'fa-times-circle'
            }
        }
        
        context.update({
            'status_groups': status_groups,
            'designers': EmployeeModel.objects.filter(role__title='Дизайнер'),
            'Status': LeadModel.Status  # Для доступа к choices в шаблоне
        })
        context['hide_sidebar'] = True
        return context
    
def change_lead_status(request, lead_id, new_status):
    lead = get_object_or_404(LeadModel, pk=lead_id)
    
    if new_status == LeadModel.Status.IN_WORK:
        # Проверяем, назначен ли дизайнер
        if not request.POST.get('designer_id'):
            messages.error(request, 'Для перевода в обработку необходимо назначить дизайнера')
            return redirect('office:kanban')
        
        designer = get_object_or_404(EmployeeModel, pk=request.POST['designer_id'], role__title='Дизайнер')
        lead.manager = designer
    
    try:
        lead.status = new_status
        lead.save()
        messages.success(request, 'Статус лида успешно обновлен')
    except ValidationError as e:
        messages.error(request, str(e))
    
    return redirect('office:kanban')
