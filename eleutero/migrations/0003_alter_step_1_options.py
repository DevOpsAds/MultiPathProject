# Generated by Django 4.2.1 on 2023-08-19 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleutero', '0002_step_1'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step_1',
            options={'ordering': ('step_number', 'command_fl1'), 'verbose_name': 'matrix 1', 'verbose_name_plural': ' passo'},
        ),
    ]