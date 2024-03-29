# Generated by Django 4.2.1 on 2023-06-27 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relacionChip', '0004_remove_mineralandia_numero_mineralandia_nome_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mineralandia',
            old_name='nome',
            new_name='code',
        ),
        migrations.AddField(
            model_name='mineralandia',
            name='Telefone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oneToOne', to='relacionChip.telefone'),
        ),
        migrations.AlterField(
            model_name='mineralandia',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Telefone', to='relacionChip.telefone'),
        ),
        migrations.AlterField(
            model_name='mineralandiafornecedor',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oneTokey', to='relacionChip.telefone'),
        ),
    ]
