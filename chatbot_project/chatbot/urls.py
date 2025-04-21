from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # frontend
    path('get_response/', views.get_response),  # backend API
]
