from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from agendapi.models import Usuario, Tipo, Agenda , Compromisso , AgendaCompromisso


# serialers define API  representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'senha',)


class TiposSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'nome', 'descricao',)

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'visivel', 'usuario', 'usercreator', 'tipo', 'institucional',)

class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compromisso
        fields = ('id', 'nome', 'datahorainicial', 'datahorafim', 'agenda',)

class AgendaCompromissoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgendaCompromisso
        fields = ('id', 'agenda', 'compromisso', 'usuarios', 'compartilhar', 'useradmin' ,'checkin',)

