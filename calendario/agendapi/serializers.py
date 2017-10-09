from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from agendapi.models import Usuario


# serialeras define API  representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url', 'nome', 'senha', 'is_staff')
