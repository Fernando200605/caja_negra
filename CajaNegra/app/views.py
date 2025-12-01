from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
# Create your views here.

PRODUCTOS = {
    1:{"nombre": "Teclado", 'stock': 10 , 'categoria':'Perifericos'},
    2:{"nombre": "Mouse", 'stock': 0 , 'categoria':'perifericos'},
    3:{"nombre": "Monitor", 'stock': 5 , 'categoria':'perifericos'},
}

def detalle_producto(request,id):
    producto = PRODUCTOS.get(id)#traemos el producto segun su id
    
    if producto is None:
        raise Http404("Error 404 manual: Producto no encontrado")
    
    if producto['stock'] == 0:
        return HttpResponse("Error 409 manual: Producto sin stock", status=409)
    
    return JsonResponse({
        "id": id,
        "nombre": producto['nombre'],
        "stock": producto['stock'],
    })

def listar_productos(request):
    repuesta = ""
    for key, value in PRODUCTOS.items():
        repuesta += f"ID: {key} - Nombre: {value['nombre']} - Stock: {value['stock']} - Categoria: {value['categoria']}<br>"
    return HttpResponse(repuesta)
    

def productos_por_categoria(request,categoria):
    categoria = categoria.lower()
    total = 0
    for key, value in PRODUCTOS.items():
        if value.get('categoria','').lower() == categoria:
            total += 1
    if total == 0:
        return HttpResponse("Error 404 manual: No hay productos en esta categoria", status=404)
    return JsonResponse({
        "mensaje":"Productos Filtrados",
        "categoria":categoria,
        "total": total,
    })
def pedidos_por_urgencia(request,anio,nivel):
    return JsonResponse({
        "mensaje":"Pedidos Filtrados",
        "anio":anio,
        "nivel":nivel,
        "coincidecias":[
            {"id":101,"descripcion":f"Pedido {nivel}"},
            {"id":102,"descripcion":f"Pedido {nivel}"},
        ]
    })

def saludar_usuario(request,user):
    return HttpResponse(f"Hola, bienvenido/a {user} a nuestra plataforma.")

  
def calculadora(request, operacion, a, b):

    if operacion == "suma":
        resultado = a + b

    elif operacion == "resta":
        resultado = a - b

    elif operacion == "multiplicacion":
        resultado = a * b

    elif operacion == "division":
        if b == 0:
            return HttpResponse("Error: división por cero")
        resultado = a / b

    else:
        raise Http404("Error 404 manual: Operación no encontrada")

    return HttpResponse(f"El resultado es {resultado}")
def habitacion_inicial(request):
    return HttpResponse(
        "Estás en un pasillo oscuro. Hay puertas al 'norte' y al 'sur'. "
        "Escribe la ruta juego/mover/norte o juego/mover/sur"
    )

def mover(request, direccion):
    if direccion == "norte":
        return HttpResponse("Caíste en un pozo. Fin del juego.")
    elif direccion == "sur":
        return HttpResponse("Encontraste una puerta secreta. ¡Ganaste!")
    else:
        return HttpResponse("Esa dirección no existe. Usa norte o sur.")
