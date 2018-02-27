# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='reserva_habitacion',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Habitacion'),
        ),
        migrations.AddField(
            model_name='reserva_habitacion',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Reserva'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='regla_precio',
            name='habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Habitacion'),
        ),
        migrations.AddField(
            model_name='regla_precio',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='recorrido',
            name='provincia_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recorrido_provincia_origen', to='servicios.Provincia'),
        ),
        migrations.AddField(
            model_name='recorrido',
            name='provincias',
            field=models.ManyToManyField(related_name='recottido_provincias', to='servicios.Provincia'),
        ),
        migrations.AddField(
            model_name='recorrido',
            name='servicio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='provincia',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Pais'),
        ),
        migrations.AddField(
            model_name='pais',
            name='idioma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Idioma'),
        ),
        migrations.AddField(
            model_name='pais',
            name='moneda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Moneda'),
        ),
        migrations.AddField(
            model_name='pack',
            name='servicio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Provincia'),
        ),
        migrations.AddField(
            model_name='indisponibilidad',
            name='habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Habitacion'),
        ),
        migrations.AddField(
            model_name='indisponibilidad',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='habitacion_alojamiento_por_habitacion',
            name='habitacion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicios.Habitacion'),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='alojamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Alojamiento'),
        ),
        migrations.AddField(
            model_name='foto_servicio',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='foto_habitacion',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Habitacion'),
        ),
        migrations.AddField(
            model_name='foto_destino',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Destino'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='municipio_origen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Municipio'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='provincia_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='excursion_provincia_destino', to='servicios.Provincia'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='recorrido',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicios.Recorrido'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='reserva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Reserva'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='destino',
            name='intereses',
            field=models.ManyToManyField(blank=True, to='servicios.Interes'),
        ),
        migrations.AddField(
            model_name='destino',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Provincia'),
        ),
        migrations.AddField(
            model_name='citytour',
            name='recorrido',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicios.Recorrido'),
        ),
        migrations.AddField(
            model_name='cancelacion_reserva',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Reserva'),
        ),
        migrations.AddField(
            model_name='alojamiento_sin_finalizar',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Municipio'),
        ),
        migrations.AddField(
            model_name='alojamiento_sin_finalizar',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Pais'),
        ),
        migrations.AddField(
            model_name='alojamiento_sin_finalizar',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Provincia'),
        ),
        migrations.AddField(
            model_name='alojamiento_sin_finalizar',
            name='tipo_alojamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.Tipo_Alojamiento'),
        ),
        migrations.AddField(
            model_name='alojamiento_sin_finalizar',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='alojamiento_completo',
            name='alojamiento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicios.Alojamiento'),
        ),
        migrations.AddField(
            model_name='alojamiento',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Municipio'),
        ),
        migrations.AddField(
            model_name='alojamiento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Pais'),
        ),
        migrations.AddField(
            model_name='alojamiento',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Provincia'),
        ),
        migrations.AddField(
            model_name='alojamiento',
            name='servicio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='alojamiento',
            name='tipo_alojamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Tipo_Alojamiento'),
        ),
    ]