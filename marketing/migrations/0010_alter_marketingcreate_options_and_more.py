# Generated by Django 4.2.1 on 2023-08-22 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0009_alter_spending_options_alter_spending_description_and_more'),
        ('marketing', '0009_marketingaddsuppliers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marketingcreate',
            options={'ordering': ('market_classify',), 'verbose_name': 'Crie um mercado', 'verbose_name_plural': '+ Criar mercados'},
        ),
        migrations.AlterField(
            model_name='marketingcreate',
            name='classify_market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomizingSpend', to='expense.customizingspend', verbose_name='personalisão das despesas'),
        ),
        migrations.AlterField(
            model_name='marketingcreate',
            name='market_classify',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Titulo para o mercado'),
        ),
        migrations.AlterField(
            model_name='marketingcreate',
            name='spending_market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spending_fk', to='expense.spending', verbose_name='tratamento de despesa'),
        ),
    ]