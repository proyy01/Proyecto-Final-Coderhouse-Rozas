# Generated by Django 5.1 on 2024-09-06 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_procesadores_imagen_delete_procesadorimagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='coolers',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenesproductos/'),
        ),
        migrations.AddField(
            model_name='monitores',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenesproductos/'),
        ),
        migrations.AddField(
            model_name='ram',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenesproductos/'),
        ),
        migrations.AddField(
            model_name='tarjetas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenesproductos/'),
        ),
    ]
