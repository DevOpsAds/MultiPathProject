# Generated by Django 4.2.1 on 2023-06-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_remove_ca_novo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'paymentmethod',
                'verbose_name_plural': 'meios de pagamentos',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='ca',
            options={'ordering': ('name',), 'verbose_name': 'checkaccount', 'verbose_name_plural': 'contas (ca)'},
        ),
        migrations.AlterField(
            model_name='ca',
            name='name',
            field=models.CharField(help_text='Digite o nome da conta check account', max_length=50, verbose_name='nome'),
        ),
    ]
