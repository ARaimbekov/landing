from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.get_file, name='download'),
    path('download2/', views.get_file2, name='download2'),
    path('download3/', views.get_file3, name='download3'),
    path('download4/', views.get_file4, name='download4'),
    path('portfoliodetails/', views.portfolio, name='portfoliodetails'),
]
