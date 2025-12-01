from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404


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


# Create your views here.
