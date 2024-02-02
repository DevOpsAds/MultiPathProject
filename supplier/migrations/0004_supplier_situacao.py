# Generated by Django 4.2.1 on 2023-07-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_supplier_grup'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='situacao',
            field=models.CharField(blank=True, choices=[('criado', 'criado'), ('Analise', 'Analise'), ('Avaliado', 'Avaliado'), ('Pendente', 'Pendente'), ('Aprovado', 'Aprovado')], max_length=20, null=True),
        ),
    ]
