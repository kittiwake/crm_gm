from django.urls import path

from office.views import KanbanBoardView, change_lead_status

app_name = 'office'
urlpatterns = [
    path('kanban/', KanbanBoardView.as_view(), name='kanban'),
    path('<int:lead_id>/change-status/<str:new_status>/', change_lead_status, name='change_status'),
]