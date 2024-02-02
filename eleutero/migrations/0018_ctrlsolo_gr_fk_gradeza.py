# Generated by Django 4.2.1 on 2023-08-22 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_base_name_options'),
        ('eleutero', '0017_alter_ctrlsolo_gr_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctrlsolo_gr',
            name='fk_gradeza',
            field=models.ForeignKey(help_text='Para Registros de unidades de medidas na base em sistema @admin', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_gradeza', to='app.grandeza', verbose_name='Registro de Medidas'),
        ),
    ]