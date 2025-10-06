from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/dashboard/', views.DashboardAPIView.as_view(), name='api-dashboard'),
]