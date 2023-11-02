from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminlog', views.adminlog, name='adminlog'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('update_theme', views.update_theme, name='update_theme'),
    path('christmas', views.christmas, name='christmas'),
    path('onam',views.onam,name='onam'),
]