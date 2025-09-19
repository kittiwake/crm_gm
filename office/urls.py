from django.urls import path

from office.views import KanbanBoardView, Order, change_lead_status

app_name = 'office'
urlpatterns = [
    path('kanban/', KanbanBoardView.as_view(), name='kanban'),
    path('<int:lead_id>/change-status/<str:new_status>/', change_lead_status, name='change_status'),
    path('order/<int:id>/', Order.as_view(), name='order_detail'),
    path('order/<int:id>/set-plan-date/', Order.as_view(), name='set_plan_date'),
    path('order/<int:id>/update-etap/', Order.as_view(), name='update_etap'),
    
]