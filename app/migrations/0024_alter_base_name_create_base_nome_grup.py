# Generated by Django 4.2.1 on 2023-08-21 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_name_base_convert_evento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base_name_create',
            name='base_nome_grup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indice_base_name', to='app.base_name', verbose_name='indice de grupos'),
        ),
    ]
