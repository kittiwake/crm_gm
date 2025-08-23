from django.urls import path
from config import settings
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='authorisation'),
]