
from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('edit-user/<int:pk>/',views.edit_user,name="edit-user"),
    path('del-user/<int:pk>/',views.del_user,name="del-user"),
    path('update-user/',views.update_user,name="update-user"),
    
    
]
