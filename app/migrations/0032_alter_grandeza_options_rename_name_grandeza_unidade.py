# Generated by Django 4.2.1 on 2023-08-22 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_grandeza_options_alter_grandeza_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grandeza',
            options={'ordering': ('index', 'unidade'), 'verbose_name': 'Criar grandeza', 'verbose_name_plural': 'Criar grandezas'},
        ),
        migrations.RenameField(
            model_name='grandeza',
            old_name='name',
            new_name='unidade',
        ),
    ]
