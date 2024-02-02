# Generated by Django 4.2.1 on 2023-06-02 02:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0025_alter_checkaccount_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privilegesaccount',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
