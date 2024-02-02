# Generated by Django 4.2.1 on 2023-08-21 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_convert_name_base_create_vl_apresentado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='name_base_convert',
            options={'ordering': ('vl_apresentado', 'index', 'pk'), 'verbose_name': 'duple de unidade', 'verbose_name_plural': 'duple de unidades'},
        ),
        migrations.AlterField(
            model_name='name_base_convert',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_base2', to='app.base_name', verbose_name='apresentado'),
        ),
        migrations.AlterField(
            model_name='name_base_convert',
            name='vl_apresentado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_base1', to='app.base_name', verbose_name='apresentado'),
        ),
    ]
