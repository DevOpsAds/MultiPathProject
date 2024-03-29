# Generated by Django 4.2.1 on 2023-06-03 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0029_imposto'),
    ]

    operations = [
        migrations.AddField(
            model_name='imposto',
            name='I_Estadual',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='I.Estadual'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imposto',
            name='I_federal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='I.Federal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imposto',
            name='n_imposto',
            field=models.CharField(blank=True, help_text='Digite o nome do imposto', max_length=20, null=True, verbose_name='imposto nome'),
        ),
        migrations.AlterField(
            model_name='imposto',
            name='taxa',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='taxa %'),
        ),
    ]
