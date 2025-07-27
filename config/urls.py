"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from config import settings
from office.views import  CreateLead, CreateOrder, Timetable, Order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Timetable.as_view(), name='timetable'),
    path('order/<int:id>', Order.as_view(), name='order'),
    path('order/set-plan-date/', Order.as_view(), name='set_plan_date'),
    path('create-lead/', CreateLead.as_view(), name='create_lead'),
    path('create-order/', CreateOrder.as_view(), name='create_order'),  # Без лида
    path('create-order/<int:lead_id>/', CreateOrder.as_view(), name='create_order_from_lead'),     
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns