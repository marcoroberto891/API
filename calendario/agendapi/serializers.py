from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from agendapi.models import Usuario, Tipo


# serialers define API  representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'senha',)


class TiposSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'nome', )
