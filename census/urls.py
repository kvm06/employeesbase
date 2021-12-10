from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('', views.list, name='list'),
    path('edit/<int:employee_id>/', views.edit, name='edit'),
    path('delete/<int:employee_id>/', views.delete, name='delete'),
    path('adddepartment', views.add_department, name='add_department'),
    path('addlanguage', views.add_language, name='add_language'),
    path('success', views.success, name='success')

]