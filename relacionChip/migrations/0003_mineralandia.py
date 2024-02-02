# Generated by Django 4.2.1 on 2023-06-27 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relacionChip', '0002_alter_telefone_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mineralandia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=11, unique=True)),
                ('cliente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oneToOne', to='relacionChip.telefone')),
            ],
        ),
    ]
