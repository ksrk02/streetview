from django.urls import path

from . import views

app_name = 'geomap'

urlpatterns = [
    path('', views.geomap_view, name='index'),
]