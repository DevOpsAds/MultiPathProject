# Generated by Django 4.2.1 on 2023-08-21 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_basenameconvert_base_nome_grup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name_base_convert',
            name='evento',
        ),
        migrations.DeleteModel(
            name='basenameConvert',
        ),
    ]