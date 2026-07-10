from django.contrib import admin
from django.urls import path
from results import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('result/', views.home, name='result'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]