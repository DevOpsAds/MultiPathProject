# Generated by Django 4.2.1 on 2023-08-23 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleutero', '0018_ctrlsolo_gr_fk_gradeza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ctrlsolo_gr',
            name='fk_base_name',
        ),
    ]
