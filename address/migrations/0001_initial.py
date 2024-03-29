# Generated by Django 4.2.1 on 2023-07-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='cidade')),
                ('uf', models.CharField(choices=[('UF', 'Estado'), ('MG', 'Minas Gerais'), ('SP', 'São paulo'), ('RJ', 'Rio de Janeiros'), ('ES', 'Espirito Santo')], max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'cidade',
                'verbose_name_plural': 'cidades',
                'ordering': ('name',),
            },
        ),
    ]
