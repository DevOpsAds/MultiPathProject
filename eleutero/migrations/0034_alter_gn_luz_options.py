# Generated by Django 4.2.1 on 2023-09-08 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleutero', '0033_alter_gn_options_alter_gn_ceu_terra_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gn_luz',
            options={'ordering': ('situacao', 'coluna', 'index', 'call', 'evento_permitido', 'txt_referncial', 'txt_name'), 'verbose_name': 'A luz', 'verbose_name_plural': 'Gênesis execulte'},
        ),
    ]