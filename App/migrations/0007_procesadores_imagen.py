# Generated by Django 5.1 on 2024-09-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_ram_velocidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='procesadores',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenesproductos/'),
        ),
    ]
