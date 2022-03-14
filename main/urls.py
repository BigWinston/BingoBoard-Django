from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board', views.board, name='board'),
    path('staff', views.staff, name='staff'),
    path('projects', views.projects, name='projects'),
    path('customers', views.customers, name='customers'),
    path('locations', views.locations, name='locations'),
    path('assignments', views.assignments, name='assignments'),
    path('backlog', views.backlog, name='backlog'),
    path('help', views.help, name='help'),
]