# Generated by Django 4.2.1 on 2023-08-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_callmymother_options_alter_callmymother_call'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grandeza',
            name='id',
        ),
        migrations.AddField(
            model_name='grandeza',
            name='callmymother_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.callmymother'),
            preserve_default=False,
        ),
    ]