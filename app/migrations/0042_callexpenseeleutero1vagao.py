# Generated by Django 4.2.1 on 2023-08-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_regions_fk_matrix'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallExpenseEleutero1vagao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call', models.IntegerField(blank=True, null=True, verbose_name='call')),
                ('fk_matrix', models.BooleanField(default=True, help_text='Activated this process.', verbose_name='Conect at matrix')),
                ('matrix_evolution', models.CharField(max_length=255, verbose_name='Object')),
            ],
            options={
                'verbose_name': 'evolution',
                'verbose_name_plural': '|__[Matrix]²£__|',
                'ordering': ('call', 'fk_matrix', 'matrix_evolution'),
            },
        ),
    ]