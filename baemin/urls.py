from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/new/', views.order_new),
    path('profile/', views.profile, name='profile'),
]
