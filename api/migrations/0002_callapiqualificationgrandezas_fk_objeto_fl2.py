# Generated by Django 4.2.1 on 2023-08-28 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fl2', '__first__'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='callapiqualificationgrandezas',
            name='fk_objeto_fl2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='un_fk_criar_obje_fl2_step_2', to='fl2.fl2_step_2', verbose_name='Objeto'),
            preserve_default=False,
        ),
    ]