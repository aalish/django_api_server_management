from django.urls import path
from .views import execute_script

urlpatterns = [
    path('execute_script/', execute_script, name='execute_script'),
]
