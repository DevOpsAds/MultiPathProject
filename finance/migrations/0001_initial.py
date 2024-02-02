# Generated by Django 4.2.1 on 2023-06-01 14:53

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
            name='Ca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Digite o nome da conta', max_length=50, verbose_name='nome')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)screate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'checkaccount',
                'verbose_name_plural': 'checkaccounts',
                'ordering': ('name',),
            },
        ),
    ]
