from django.urls import include, path
from .views import PlanCeh

urlpatterns = [
    path('ceh/<str:ceh_code>', PlanCeh.as_view(), name='planceh'),
]