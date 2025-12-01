from django.urls import path

from app.views import * 

urlpatterns = [
    path('habitacion/1/', views.habitacion_inicial, name='habitacion'),
    path('mover/<str:direccion>/', views.mover, name='mover'),
]
