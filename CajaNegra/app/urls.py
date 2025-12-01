from django.urls import path

from app.views import * 

urlpatterns = [
    path('habitacion/1/', habitacion_inicial, name='habitacion'),
    path('mover/<str:direccion>/', mover, name='mover'),
]
