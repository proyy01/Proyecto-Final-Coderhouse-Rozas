# Generated by Django 5.1 on 2024-09-05 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_procesadores_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procesadores',
            name='imagen',
        ),
        migrations.CreateModel(
            name='ProcesadorImagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='procesadorimagenes')),
                ('procesador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.procesadores')),
            ],
        ),
    ]
