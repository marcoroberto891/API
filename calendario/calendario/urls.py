"""calendario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin
from agendapi.models import Tipo
from rest_framework import routers, serializers, viewsets
from agendapi.views import UsersViewSet,TiposViewSet

router = routers.DefaultRouter()
router.register(r'USERS', UsersViewSet)
router.register(r'TIPOS', TiposViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^Tipos/', Tipo,name='listaTipos'),
    # url(r'^Compromissos/', index, name='index'),
    # url(r'^Usuarios/', index, name='index'),
    # url(r'^Agenda Compromissos/', index, name='index'),
    # url(r'^Agenda Usuarios/', index, name='index')
]
