# Generated by Django 4.2.1 on 2023-08-21 17:10

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
            name='val_Fl1',
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
                ('evento_permitido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriz_Eleutero', to='eleutero.fl1', verbose_name='matrix_eleutero')),
                ('grup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup')),
                ('pk_created_user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)screate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'val_matrix',
                'verbose_name_plural': 'valores_matrices',
                'ordering': ('matx_name', 'evento_permitido'),
            },
        ),
    ]
