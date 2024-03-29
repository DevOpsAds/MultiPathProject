# Generated by Django 4.2.1 on 2023-08-17 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_alter_spending_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingcreate',
            name='classify_market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomizingSpend', to='expense.customizingspend', verbose_name=' +prod. encontrados'),
        ),
        migrations.CreateModel(
            name='MarketingAddSuppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('situacao', models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Avaliando'), ('4', 'Analise'), ('5', 'Paralizado'), ('6', 'Pendente'), ('7', 'Negado')], default=2, max_length=20, null=True)),
                ('active', models.BooleanField(default=False, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='privilegio')),
                ('marketcreate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marketingcreate', to='marketing.marketingcreate', verbose_name='ramo')),
            ],
            options={
                'verbose_name': 'marketingaddsuppliers',
                'verbose_name_plural': 'adicão de mercados',
                'ordering': ('marketcreate',),
            },
        ),
    ]
