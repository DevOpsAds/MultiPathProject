# Generated by Django 4.2.1 on 2023-07-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0009_alter_cep_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cep',
            name='fk_tb_auto_vincu',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='fk_ resistro_vinculado'),
        ),
        migrations.AddField(
            model_name='cep',
            name='tb_cep_vinculado',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='auto_'),
        ),
    ]