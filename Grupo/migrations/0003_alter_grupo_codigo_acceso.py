# Generated by Django 4.1.6 on 2025-05-10 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grupo', '0002_alter_grupo_codigo_acceso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='codigo_acceso',
            field=models.CharField(max_length=100),
        ),
    ]
