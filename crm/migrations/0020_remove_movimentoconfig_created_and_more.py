# Generated by Django 4.2.1 on 2023-08-21 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_cobine_convert_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentoconfig',
            name='created',
        ),
        migrations.RemoveField(
            model_name='movimentoconfig',
            name='modified',
        ),
    ]