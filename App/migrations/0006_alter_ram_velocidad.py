# Generated by Django 5.1 on 2024-09-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_coolers_modelo_monitores_modelo_ram_modelo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ram',
            name='velocidad',
            field=models.CharField(max_length=40),
        ),
    ]
