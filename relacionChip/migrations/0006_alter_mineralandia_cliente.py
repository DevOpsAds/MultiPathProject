# Generated by Django 4.2.1 on 2023-06-27 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relacionChip', '0005_rename_nome_mineralandia_code_mineralandia_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineralandia',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Telefone', to='relacionChip.cliente'),
        ),
    ]