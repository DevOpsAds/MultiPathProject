# Generated by Django 4.2.1 on 2023-09-02 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_photo_fk_matrix'),
        ('eleutero', '0027_gn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gn',
            name='evento_permitido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_crm', to='crm.movimentoconfig', verbose_name='Mov.conf.'),
        ),
    ]
