# Generated by Django 4.2.1 on 2023-09-09 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supplier', '0014_alter_meterorologia_coleta_and_more'),
        ('eleutero', '0034_alter_gn_luz_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='gn',
            name='registro_meterorologia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_in_met', to='supplier.meterorologia', verbose_name='Reg.met.'),
        ),
        migrations.AddField(
            model_name='gn_ceu_terra',
            name='registro_meterorologia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_met', to='supplier.meterorologia', verbose_name='Reg.met.'),
        ),
        migrations.AddField(
            model_name='gn_luz',
            name='registro_meterorologia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='in_met', to='supplier.meterorologia', verbose_name='Reg.met.'),
        ),
        migrations.AlterField(
            model_name='gn_luz',
            name='evento_matrix',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GN_in_fk_matrix', to='eleutero.gn', verbose_name='config_Gênesis..'),
        ),
        migrations.CreateModel(
            name='Gn_noite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('situacao', models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Avaliando'), ('4', 'Analise'), ('5', 'Paralizado'), ('6', 'Pendente'), ('7', 'Negado')], default=2, max_length=20, null=True)),
                ('active', models.BooleanField(default=False, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('inicio_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='data/hora', null=True, verbose_name='início/comerço')),
                ('fim_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='data/hora', null=True, verbose_name='fim/termino')),
                ('index', models.IntegerField(help_text='linha ..', verbose_name='index l.')),
                ('coluna', models.CharField(help_text='coluna ..', max_length=15, verbose_name='col.')),
                ('call', models.IntegerField(help_text='piso ..', verbose_name='call')),
                ('txt_name', models.CharField(max_length=150, verbose_name='nome')),
                ('txt_referncial', models.CharField(blank=True, max_length=15, null=True, verbose_name='ref./*')),
                ('mem_description', models.TextField(blank=True, null=True, verbose_name='descreva')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='privilegio')),
                ('created_user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)screate', to=settings.AUTH_USER_MODEL)),
                ('evento_detalhadi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eleutero_fk_detalhado', to='eleutero.gn_ceu_terra', verbose_name='conf.evento.')),
                ('evento_matrix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_GN', to='eleutero.gn', verbose_name='config_Gênesis..')),
                ('evento_permitido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_in_eleutero_fk_fk', to='eleutero.gn_luz', verbose_name='conf.detalhado em evento.')),
                ('grup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup')),
                ('registro_meterorologia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_at_met', to='supplier.meterorologia', verbose_name='Reg.met.')),
            ],
            options={
                'verbose_name': 'A Noite',
                'verbose_name_plural': 'Gênesis horarios e detalhes',
                'ordering': ('inicio_date', 'fim_date', 'situacao', 'coluna', 'index', 'call', 'evento_permitido', 'txt_referncial', 'txt_name'),
            },
        ),
    ]
