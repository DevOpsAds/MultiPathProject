# Generated by Django 4.2.1 on 2023-08-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleutero', '0023_alter_sendbigdata_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendbigdata',
            options={'ordering': ('index',), 'verbose_name': 'CALL: my mother now'},
        ),
        migrations.AddField(
            model_name='sendbigdata',
            name='fk_matrix',
            field=models.BooleanField(default=True, help_text='habiliter this process.', verbose_name='conectar a matrix'),
        ),
        migrations.AddField(
            model_name='sendbigdata',
            name='matrix_evolution',
            field=models.CharField(default='big data', max_length=255, verbose_name='Objeto'),
            preserve_default=False,
        ),
    ]
