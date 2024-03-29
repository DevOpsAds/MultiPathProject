# Generated by Django 4.2.1 on 2023-08-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_callapiqualificationgrandezas_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallApiQualification_grandezas_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call', models.IntegerField(blank=True, null=True, verbose_name='call')),
                ('fk_matrix', models.BooleanField(default=True, help_text='Activated this process.', verbose_name='Conect at matrix')),
                ('matrix_evolution', models.CharField(max_length=255, verbose_name='Object')),
            ],
            options={
                'verbose_name': 'medida em pessoa',
                'verbose_name_plural': 'MTX|medidas em pessoas',
                'ordering': ('call', 'fk_matrix', 'matrix_evolution'),
            },
        ),
        migrations.AlterModelOptions(
            name='callapiqualificationgrandezas',
            options={'ordering': ('matx_name',), 'verbose_name': 'dimensão e medida', 'verbose_name_plural': 'dimensões e medidas'},
        ),
    ]
