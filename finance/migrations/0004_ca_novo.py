# Generated by Django 4.2.1 on 2023-06-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_alter_ca_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='novo',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]