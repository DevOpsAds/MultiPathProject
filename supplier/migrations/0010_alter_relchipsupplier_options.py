# Generated by Django 4.2.1 on 2023-08-18 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0009_alter_supplier_options_relchipsupplier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relchipsupplier',
            options={'ordering': ('situacao', '-active', 'exist_deleted', 'reltrade_name'), 'verbose_name': 'fornecedor', 'verbose_name_plural': 'fornecedores'},
        ),
    ]
