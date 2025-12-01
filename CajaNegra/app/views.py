from django.shortcuts import render


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
