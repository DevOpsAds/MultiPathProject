# Generated by Django 4.2.1 on 2023-08-21 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_name_base_convert_function_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='name_base_convert',
            options={'ordering': ('function_name', 'index', 'pk'), 'verbose_name': 'C) Criar cobinação', 'verbose_name_plural': 'C) Criar cobinações'},
        ),
        migrations.AlterField(
            model_name='name_base_convert',
            name='name',
            field=models.ManyToManyField(related_name='name_base1', to='app.base_name_create', verbose_name='apresentado'),
        ),
    ]
