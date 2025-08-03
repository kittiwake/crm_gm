from django.urls import path
from .views import EmployeeManagementView, get_employee_data, save_employee, toggle_employee_status

urlpatterns = [
    path('', EmployeeManagementView.as_view(), name='employee_management'),
    path('save/', save_employee, name='save_employee'),
    path('toggle-status/<int:employee_id>/', toggle_employee_status, name='toggle_employee_status'),
    path('get/<int:employee_id>/', get_employee_data, name='get_employee_data'),
]