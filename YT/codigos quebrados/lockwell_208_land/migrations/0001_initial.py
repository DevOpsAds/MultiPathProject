# Generated by Django 4.2.1 on 2023-06-23 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mtb_Matrix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matx_name', models.CharField(max_length=255, verbose_name='nome')),
                ('progress', models.CharField(choices=[('texting', 'Texting'), ('creating', 'Creating'), ('doing', 'Doing'), ('done', 'Done')], max_length=8)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)screate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'matrix',
                'verbose_name_plural': 'matrices',
                'ordering': ('pk',),
            },
        ),
    ]