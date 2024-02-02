# Generated by Django 4.2.1 on 2023-06-01 19:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0012_privilegesaccount_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='privilegesaccount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='privilegesaccount',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]