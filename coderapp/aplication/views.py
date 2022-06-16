from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from aplication.models import Familiar


def parientes(self):
    familiar1 = Familiar (nombre="rosa",edad=67, fecha_nacimiento="1954-03-23", parentesco="mama")
    familiar1.save()

    familiar2 = Familiar (nombre="dai",edad=27, fecha_nacimiento="1994-03-23", parentesco="hermana")
    familiar2.save()

    familiar3 = Familiar (nombre="fer",edad=35, fecha_nacimiento="1987-05-19", parentesco="hermano")
    familiar3.save()

    respuesta=f"Mi familiares son {familiar1.nombre}, {familiar1.edad}, {familiar1.fecha_nacimiento},{familiar1.parentesco},{familiar2.nombre}, {familiar2.edad}, {familiar2.fecha_nacimiento},{familiar2.parentesco},{familiar3.nombre}, {familiar3.edad}, {familiar3.fecha_nacimiento},{familiar3.parentesco}"

    return HttpResponse(respuesta)