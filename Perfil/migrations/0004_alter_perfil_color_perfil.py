# Generated by Django 4.1.6 on 2025-05-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0003_perfil_color_perfil_perfil_foto_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='color_perfil',
            field=models.CharField(default='#f0f2f5', max_length=20),
        ),
    ]
