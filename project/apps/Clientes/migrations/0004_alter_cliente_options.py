# Generated by Django 4.2.4 on 2023-08-08 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_cliente_proyecto_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
    ]
