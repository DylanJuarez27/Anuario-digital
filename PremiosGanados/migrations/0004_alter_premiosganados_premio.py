# Generated by Django 4.1.6 on 2025-05-17 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Premio', '0001_initial'),
        ('PremiosGanados', '0003_premiosganados_fecha_ganado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiosganados',
            name='premio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Premio.premio'),
        ),
    ]
