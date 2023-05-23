# Generated by Django 4.2.1 on 2023-05-18 20:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='endereço')),
                ('address_number', models.IntegerField(blank=True, null=True, verbose_name='número')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='complemento')),
                ('district', models.CharField(blank=True, max_length=100, null=True, verbose_name='bairro')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('country', models.CharField(blank=True, default='Brasil', max_length=50, null=True, verbose_name='país')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=11, null=True, verbose_name='RG')),
                ('cnh', models.CharField(blank=True, max_length=20, null=True, verbose_name='CNH')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('first_name', models.CharField(help_text='Digite somente o primeiro nome.', max_length=50, verbose_name='nome')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='sobrenome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'pessoa',
                'verbose_name_plural': 'pessoas',
                'ordering': ('first_name',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='foto')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='crm.person', verbose_name='foto')),
            ],
            options={
                'verbose_name': 'foto',
                'verbose_name_plural': 'fotos',
                'ordering': ('pk',),
            },
        ),
    ]
