from django.urls import path

from app.views import * 

urlpatterns = [
    path('calculadora/<str:operacion>/<int:a>/<int:b>/', calculadora),
]
