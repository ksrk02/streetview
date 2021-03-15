from django.urls import path

from . import views

app_name = 'streetview'

urlpatterns = [
    path('', views.scene_view, name='view'),
    path('ajax/', views.ajax_transition, name='ajax_transition'),
]