from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('requests/<int:request_id>/', views.update_request, name='update_request'),
]
