# Generated by Django 4.2.1 on 2023-08-19 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleutero', '0003_alter_step_1_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step_1',
            name='created',
        ),
        migrations.RemoveField(
            model_name='step_1',
            name='modified',
        ),
    ]
