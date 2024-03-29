# Generated by Django 4.2.1 on 2023-09-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleutero', '0029_alter_gn_call_alter_gn_coluna_alter_gn_index_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gn',
            name='mem_description',
            field=models.TextField(blank=True, null=True, verbose_name='descreva'),
        ),
        migrations.AlterField(
            model_name='gn',
            name='txt_referncial',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='ref./*'),
        ),
        migrations.AlterField(
            model_name='gn_ceu_terra',
            name='mem_description',
            field=models.TextField(blank=True, null=True, verbose_name='descreva'),
        ),
        migrations.AlterField(
            model_name='gn_ceu_terra',
            name='txt_referncial',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='ref./*'),
        ),
    ]
