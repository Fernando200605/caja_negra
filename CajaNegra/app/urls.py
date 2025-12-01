from django.urls import path

from app.views import * 

urlpatterns = [
    # Rutas de productos
    path("producto/<int:id>/", detalle_producto),            
    path("producto/categoria/<str:categoria>/", productos_por_categoria),
    path("producto/listar/", listar_productos),
    #rutas de pedidos
    path("pedidos/<int:anio>/<str:nivel>/",pedidos_por_urgencia),
    #ruta de saludo
    path("usuario/<str:user>/", saludar_usuario),
    #Ruta Actividad 2
    path('calculadora/<str:operacion>/<int:a>/<int:b>/', calculadora),
    #Ruta Actividad 3
    path('habitacion/1/', habitacion_inicial, name='habitacion'),
    path('mover/<str:direccion>/', mover, name='mover'),
]

