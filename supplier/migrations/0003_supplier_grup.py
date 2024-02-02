# Generated by Django 4.2.1 on 2023-07-29 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('supplier', '0002_alter_supplier_interesses'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='grup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup'),
        ),
    ]
