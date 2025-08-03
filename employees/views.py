from django.views.generic import TemplateView
from django.shortcuts import redirect

from .models import EmployeeModel, RoleModel
from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import random
import string

class EmployeeManagementView(TemplateView):
    template_name = "employee_management.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = RoleModel.objects.prefetch_related('employees').all()
        return context


def save_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        try:
            if employee_id:  # Редактирование
                employee = EmployeeModel.objects.get(pk=employee_id)
            else:  # Создание
                employee = EmployeeModel()

            # Обновляем основные данные
            employee.first_name = request.POST.get('first_name', '')
            employee.last_name = request.POST.get('last_name', '')
            employee.email = request.POST.get('email', '')
            employee.phone = request.POST.get('phone', '')
            employee.tg_nickname = request.POST.get('telegram', '')
            employee.is_active = request.POST.get('is_active') == 'on'
            
            role_id = request.POST.get('role')
            if role_id:
                try:
                    employee.role = RoleModel.objects.get(pk=role_id)
                except RoleModel.DoesNotExist:
                    pass
            
            # employee.save()

            generate_account = request.POST.get('generate_account') == 'on' and not employee_id

            response_data = {'success': True}
            
            if generate_account and not employee.user:
                # Генерация учетных данных только для новых сотрудников
                login = request.POST.get('generated_login', '')
                password = request.POST.get('generated_password', '')

                user = User.objects.create_user(
                    username=login,
                    password=password,
                )

                employee.user = user
                employee.save()
                
                response_data['login'] = login
                response_data['password'] = password


            return JsonResponse(response_data)
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def get_employee_data(request, employee_id):
    try:
        employee = EmployeeModel.objects.get(pk=employee_id)
        data = model_to_dict(employee)
        data['role_id'] = employee.role.id if employee.role else None
        
        # Добавляем данные из профиля пользователя, если есть
        if employee.user:
            data['telegram'] = employee.tg_nickname or ''
            data['has_account'] = True
        else:
            data['telegram'] = ''
            data['has_account'] = False
            
        return JsonResponse({'success': True, 'employee': data})
    except EmployeeModel.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Employee not found'})
    
def toggle_employee_status(request, employee_id):
    if request.method == 'POST':
        try:
            employee = EmployeeModel.objects.get(pk=employee_id)
            employee.is_active = not employee.is_active
            employee.save()
            return redirect('employee_management')
        except EmployeeModel.DoesNotExist:
            pass
    return redirect('employee_management')