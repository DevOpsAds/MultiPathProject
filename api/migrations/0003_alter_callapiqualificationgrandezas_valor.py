# Generated by Django 4.2.1 on 2023-08-28 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_callapiqualificationgrandezas_fk_objeto_fl2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callapiqualificationgrandezas',
            name='valor',
            field=models.FloatField(blank=True, help_text='Entre com o valor coletado', null=True, verbose_name='valor'),
        ),
    ]
