# Generated by Django 4.2.1 on 2023-08-22 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_alter_grandeza_unidade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='base_name',
            options={'ordering': ('index', 'name'), 'verbose_name': 'A) Criar unidade', 'verbose_name_plural': 'A) Criar medidas e unidades'},
        ),
    ]
