# Generated by Django 4.2.1 on 2023-07-30 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_alter_person_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='situacao',
            field=models.CharField(blank=True, choices=[('criado', 'criado'), ('Analise', 'Analise'), ('Avaliado', 'Avaliado'), ('Pendente', 'Pendente'), ('Aprovado', 'Aprovado')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=False, verbose_name='ativo'),
        ),
    ]
