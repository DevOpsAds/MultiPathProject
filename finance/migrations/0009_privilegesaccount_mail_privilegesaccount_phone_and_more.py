# Generated by Django 4.2.1 on 2023-06-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_privilegesaccount_account_privilegesaccount_bank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='privilegesaccount',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='privilegesaccount',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='n° telefone'),
        ),
        migrations.AddField(
            model_name='privilegesaccount',
            name='randomKey',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='conta'),
        ),
    ]
