# Generated by Django 4.2.1 on 2023-08-21 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_basenameconvert_function_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basenameconvert',
            name='evento',
        ),
    ]
