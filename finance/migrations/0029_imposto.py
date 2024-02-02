# Generated by Django 4.2.1 on 2023-06-02 23:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0003_alter_person_created'),
        ('finance', '0028_alter_balanceinitilaccount_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='imposto',
            fields=[
                ('checkaccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finance.checkaccount')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('movement_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='data')),
                ('n_imposto', models.CharField(blank=True, help_text='Digite o nome do imposto', max_length=20, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('taxa', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='imposto %')),
                ('value_pay', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='valor')),
                ('MovimentoConfig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MovimentoConfig', to='crm.movimentoconfig', verbose_name='MovimentoConfig')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
            ],
            options={
                'abstract': False,
            },
            bases=('finance.checkaccount', models.Model),
        ),
    ]