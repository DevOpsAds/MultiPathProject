# Generated by Django 4.2.1 on 2023-08-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_grandeza_options_rename_name_grandeza_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grandeza',
            name='unidade',
            field=models.CharField(max_length=70, verbose_name='nome/unidade'),
        ),
    ]
