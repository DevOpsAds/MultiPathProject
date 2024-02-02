# Generated by Django 4.2.1 on 2023-08-17 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_alter_payment_methods_options'),
        ('marketing', '0003_remove_marketingaddsuppliers_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingaddsuppliers',
            name='marketcreate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rotina', to='crm.routine', verbose_name='ramo'),
        ),
    ]
