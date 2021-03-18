from django.urls import path

from . import views

app_name = 'scenes'

urlpatterns = [
    path('', views.scene_view, name='index'),
    path('ajax/', views.ajax_transition, name='ajax_transition'),
]