# Generated by Django 4.2.1 on 2023-08-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_routine_active_routine_created_routine_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='progress',
            field=models.CharField(choices=[('1', 'Testando'), ('2', 'Criando'), ('3', 'Negada'), ('4', 'Valendo')], max_length=8),
        ),
    ]
