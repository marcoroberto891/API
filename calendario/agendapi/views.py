from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agendapi.serializers import UserSerializer, TiposSerializer , AgendaSerializer , CompromissoSerializer
from agendapi.serializers import AgendaCompromissoSerializer
from agendapi.models import Tipo, Usuario ,Agenda , Compromisso , AgendaCompromisso


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
    serializer_class = TiposSerializer


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class CompromissoViewSet(viewsets.ModelViewSet):
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer

class AgendaCompromissoViewSet(viewsets.ModelViewSet):
    queryset = AgendaCompromisso.objects.all()
    serializer_class = AgendaCompromissoSerializer

