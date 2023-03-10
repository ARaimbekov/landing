from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.get_file, name='download'),
    path('download2/', views.get_file2, name='download2'),
    path('download3/', views.get_file3, name='download3'),
    path('download4/', views.get_file4, name='download4'),
    path('portfolio1/', views.portfolio1, name='portfolio1'),
    path('portfolio2/', views.portfolio2, name='portfolio2'),
    path('portfolio3/', views.portfolio3, name='portfolio3'),
    path('portfolio4/', views.portfolio4, name='portfolio4'),
    path('portfolio5/', views.portfolio5, name='portfolio5'),
    path('portfolio6/', views.portfolio6, name='portfolio6'),
    path('portfolio7/', views.portfolio7, name='portfolio7'),
    path('portfolio8/', views.portfolio8, name='portfolio8'),
    path('portfolio9/', views.portfolio9, name='portfolio9'),
]
