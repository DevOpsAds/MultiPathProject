# Generated by Django 4.2.1 on 2023-07-30 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_alter_person_active_alter_person_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='situacao',
            field=models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Analise'), ('4', 'Avaliado'), ('5', 'Pendente'), ('6', 'Negado')], default=2, max_length=20, null=True),
        ),
    ]
