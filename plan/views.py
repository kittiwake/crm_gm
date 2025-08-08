import json
from django.shortcuts import render
from django.utils import timezone

from office.models.order_model import OrderModel
from .models import PlanTechModel
from employees.models import EmployeeModel
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


def plan_tech_view(request):
    # Получаем конструкторов (сотрудников с соответствующей ролью)
    constructors = EmployeeModel.objects.filter(role__title='Конструктор').order_by('last_name')
    
    # Получаем заказы, которые еще не распределены
    assigned_orders = PlanTechModel.objects.values_list('order_id', flat=True)
    available_orders = OrderModel.objects.exclude(id__in=assigned_orders).order_by('term')
    
    # Получаем текущие распределения
    current_assignments = PlanTechModel.objects.select_related('order', 'employee').all()
    
    # Генерируем 5 рабочих дней начиная с текущего дня
    today = timezone.now().date()
    work_days = []
    current_day = today
    
    # Находим ближайший рабочий день (пропускаем выходные)
    while len(work_days) < 5:
        if current_day.weekday() < 5:  # 0-4 = пн-пт
            work_days.append(current_day)
        current_day += timezone.timedelta(days=1)
    
    context = {
        'constructors': constructors,
        'available_orders': available_orders,
        'current_assignments': current_assignments,
        'work_days': work_days,
    }
    
    return render(request, 'plan_tech.html', context)



@require_POST
@csrf_exempt
def assign_order(request):
    try:
        data = json.loads(request.body)
        assignment = PlanTechModel.objects.create(
            order_id=data['order_id'],
            employee_id=data['constructor_id'],
            date=data['date'],
            status='NEW'
        )
        return JsonResponse({
            'success': True,
            'assignment_id': assignment.id,
            'order_number': assignment.order.number,
            'constructor_name': assignment.employee.last_name,
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@require_POST
@csrf_exempt
def move_assignment(request):
    try:
        data = json.loads(request.body)
        assignment = PlanTechModel.objects.get(id=data['assignment_id'])
        assignment.employee_id = data['constructor_id']
        assignment.date = data['date']
        assignment.save()
        return JsonResponse({
            'success': True,
            'constructor_name': assignment.employee.last_name,
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})