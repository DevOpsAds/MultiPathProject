# Generated by Django 4.2.1 on 2023-07-01 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relacionChip', '0013_alter_city_uf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relacionChip.city', verbose_name='cidade'),
        ),
    ]
