# Generated by Django 4.2.1 on 2023-08-23 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_qualificar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('eleutero', '0021_remove_ctrlsolo_gr_movement_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendBigData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('situacao', models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Avaliando'), ('4', 'Analise'), ('5', 'Paralizado'), ('6', 'Pendente'), ('7', 'Negado')], default=2, max_length=20, null=True)),
                ('active', models.BooleanField(default=False, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('movement_date', models.DateField(blank=True, null=True, verbose_name='Registro de início')),
                ('fk_cep', models.BooleanField(default=False, help_text='Para habiliter neste processo.', verbose_name='criar a enderços')),
                ('index', models.IntegerField(verbose_name='nº')),
                ('fk_matrix', models.BooleanField(default=True, help_text='habiliter this process.', verbose_name='conectar a matris')),
                ('matrix_evolution', models.CharField(max_length=255, verbose_name='Objeto')),
                ('description', models.TextField(help_text='Resuma em 300* caracteres.', verbose_name='descreva')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='privilegio')),
                ('created_user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)screate', to=settings.AUTH_USER_MODEL)),
                ('fk_gradeza', models.ForeignKey(help_text='Para Registros de unidades de medidas na base em sistema @admin', on_delete=django.db.models.deletion.CASCADE, related_name='fk_big_gradeza', to='app.grandeza', verbose_name='Registro de Medidas')),
                ('grup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup')),
            ],
            options={
                'verbose_name': 'Criar objeto',
                'verbose_name_plural': 'Criar objetos',
                'ordering': ('index', 'matrix_evolution'),
            },
        ),
    ]
