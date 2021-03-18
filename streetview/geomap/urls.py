from django.urls import path

from . import views

app_name = 'geomap'

urlpatterns = [
    path('', views.geomap_view, name='index'),
    path('ajax/', views.ajax_fileload, name='ajax_fileload'),
]