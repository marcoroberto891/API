from django.db import models


# Create your models here.

class Tipo(models.Model):
    nome = models.CharField('nome', max_length=50)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField('nome', max_length=50)
    senha = models.CharField('nome', max_length=6)

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    visivel = models.BooleanField(blank=True)
    usuario = models.ForeignKey(Usuario, related_name='users', null=True, blank=False)
    tipo = models.ForeignKey(Tipo, related_name='tipos', null=True, blank=False)
    institucional = models.BooleanField(blank=True)

    def __str__(self):
        return self.nome


class Compromisso(models.Model):
    nome = models.CharField('nome', max_length=50)
    datahorainicial = models.DateTimeField(blank=True, null=True)
    datahorafim = models.DateTimeField()
    agenda = models.ForeignKey(Agenda, related_name='compromissos', null=True, blank=False)

    def __str__(self):
        return self.nome


class agendaCompromisso(models.Model):
    agenda = models.ForeignKey(Agenda, related_name="agendadecompromissos", null=True, blank=False)
    compromisso = models.ForeignKey(Compromisso, related_name='agendacomp', null=True, blank=False)
    usuarios = models.ForeignKey(Usuario, related_name='usersagendacomp1', null=True, blank=False)
    compartilhar = models.BooleanField(blank=True)  # permissao para visualizar
    useradmin = models.BooleanField(blank=True)  ##usuario que enviou o compartilhamento do compromisso
    checkin = models.BooleanField(blank=True)  ##usuario confirma se ira ou nao ao compromisso

    def __str__(self):
        return self.nome


class agendaUsuario(models.Model):
    agenda = models.ForeignKey(Agenda, related_name="agendacompromissos", null=True, blank=False)
    usuarios = models.ForeignKey(Usuario, related_name='usersagendacomp2', null=True, blank=False)
    compartilhar = models.BooleanField(blank=True)  ## permissao para visualizar
    useradmin = models.BooleanField(blank=True)  ##usuario que compartilhou a agenda

    def __str__(self):
        return self.nome
