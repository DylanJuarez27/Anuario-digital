# Generated by Django 4.1.6 on 2025-05-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PremiosGanados', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premiosganados',
            name='votacion',
        ),
        migrations.AddField(
            model_name='premiosganados',
            name='porcentaje_ganado',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='premiosganados',
            name='puntaje',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
