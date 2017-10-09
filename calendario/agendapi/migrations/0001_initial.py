# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visivel', models.BooleanField()),
                ('institucional', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='agendaCompromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compartilhar', models.BooleanField()),
                ('useradmin', models.BooleanField()),
                ('checkin', models.BooleanField()),
                ('agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendadecompromissos', to='agendapi.Agenda')),
            ],
        ),
        migrations.CreateModel(
            name='agendaUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compartilhar', models.BooleanField()),
                ('useradmin', models.BooleanField()),
                ('agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendacompromissos', to='agendapi.Agenda')),
            ],
        ),
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('datahorainicial', models.DateTimeField(blank=True, null=True)),
                ('datahorafim', models.DateTimeField()),
                ('agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compromissos', to='agendapi.Agenda')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('senha', models.CharField(max_length=6, verbose_name='nome')),
            ],
        ),
        migrations.AddField(
            model_name='agendausuario',
            name='usuarios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usersagendacomp2', to='agendapi.Usuario'),
        ),
        migrations.AddField(
            model_name='agendacompromisso',
            name='compromisso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendacomp', to='agendapi.Compromisso'),
        ),
        migrations.AddField(
            model_name='agendacompromisso',
            name='usuarios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usersagendacomp1', to='agendapi.Usuario'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipos', to='agendapi.Tipo'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='agendapi.Usuario'),
        ),
    ]
