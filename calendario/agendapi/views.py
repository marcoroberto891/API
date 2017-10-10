from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agendapi.serializers import UserSerializer
from agendapi.models import Tipo, Usuario


def listaTipos(request):
    retorno = "<h1>Eventos</h1>"
    lista = Tipo.objects.all()
    for tipo in lista:
        retorno += '</br>Nome do Evento:{}</br>'.format(lista.nome)
    return HttpResponse(retorno)


# ViewSets
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


class TiposViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = UserSerializer
