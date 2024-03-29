# Generated by Django 4.2.1 on 2023-08-19 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eleutero', '0010_remove_step_2_evento'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fl2_Fl1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('situacao', models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Avaliando'), ('4', 'Analise'), ('5', 'Paralizado'), ('6', 'Pendente'), ('7', 'Negado')], default=2, max_length=20, null=True)),
                ('active', models.BooleanField(default=False, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('movement_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='data')),
                ('matx_name', models.CharField(max_length=255, verbose_name='nome')),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='privilegio')),
                ('created_user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)screate', to=settings.AUTH_USER_MODEL)),
                ('fl2_evento_permitido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fl1_matrix', to='eleutero.fl1', verbose_name='matrix')),
                ('grup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup')),
            ],
            options={
                'verbose_name': 'matrix',
                'verbose_name_plural': 'matrices',
                'ordering': ('matx_name', 'fl2_evento_permitido'),
            },
        ),
        migrations.CreateModel(
            name='Fl2_Step_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('situacao', models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Avaliando'), ('4', 'Analise'), ('5', 'Paralizado'), ('6', 'Pendente'), ('7', 'Negado')], default=2, max_length=20, null=True)),
                ('active', models.BooleanField(default=False, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('movement_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='data/hora')),
                ('step_number', models.IntegerField(blank=True, null=True, verbose_name='passo')),
                ('name_step_listar', models.CharField(max_length=100, verbose_name='listar')),
                ('progress', models.CharField(choices=[('1', 'Esperando'), ('2', 'Atrasado'), ('3', 'problema'), ('4', 'Preparando')], max_length=10)),
                ('description', models.TextField()),
                ('Fl2_passo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fl2_passo', to='eleutero.step_1', verbose_name='_Fl2passo')),
                ('command_fl1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrix', to='fl2.fl2_fl1', verbose_name='autorizador')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='privilegio')),
                ('created_user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)screate', to=settings.AUTH_USER_MODEL)),
                ('grup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup')),
            ],
            options={
                'verbose_name': 'Fl2_passo',
                'verbose_name_plural': 'Fl2_passos',
                'ordering': ('step_number', 'command_fl1'),
            },
        ),
        migrations.CreateModel(
            name='Fl2_Step_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('situacao', models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Avaliando'), ('4', 'Analise'), ('5', 'Paralizado'), ('6', 'Pendente'), ('7', 'Negado')], default=2, max_length=20, null=True)),
                ('active', models.BooleanField(default=False, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('movement_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='data/hora')),
                ('step_number', models.IntegerField(blank=True, null=True, verbose_name='passo')),
                ('item_name', models.CharField(max_length=100, verbose_name='nome')),
                ('type_item', models.CharField(max_length=100, verbose_name='tipo')),
                ('progress', models.CharField(choices=[('1', 'Esperando'), ('2', 'Atrasado'), ('3', 'problema'), ('4', 'Preparando')], max_length=10)),
                ('Fl2_type_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fl2_matrix', to='eleutero.step_2', verbose_name='Fl2_tarf')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='privilegio')),
                ('grup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrix', to='fl2.fl2_step_1', verbose_name='tarf')),
            ],
            options={
                'verbose_name': 'items',
                'verbose_name_plural': 'create_my_itens',
                'ordering': ('step', 'step_number'),
            },
        ),
    ]
