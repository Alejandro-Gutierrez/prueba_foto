from django.shortcuts import render
from django.views.generic import View

from .models import *


class MostrarFotos(View):
    def get(self, request):
        datos = Mascota.objects.all()
        return render(request, 'RegistroMascota/fotos.html', {"datos":datos})

# Create your views here.
