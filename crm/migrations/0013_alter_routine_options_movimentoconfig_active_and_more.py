# Generated by Django 4.2.1 on 2023-08-18 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('crm', '0012_alter_routine_progress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='routine',
            options={'ordering': ('modulo', 'pk', 'person'), 'verbose_name': 'rotina', 'verbose_name_plural': 'routines'},
        ),
        migrations.AddField(
            model_name='movimentoconfig',
            name='active',
            field=models.BooleanField(default=False, verbose_name='ativo'),
        ),
        migrations.AddField(
            model_name='movimentoconfig',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='criado em'),
        ),
        migrations.AddField(
            model_name='movimentoconfig',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='privilegio'),
        ),
        migrations.AddField(
            model_name='movimentoconfig',
            name='exist_deleted',
            field=models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado'),
        ),
        migrations.AddField(
            model_name='movimentoconfig',
            name='grup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup'),
        ),
        migrations.AddField(
            model_name='movimentoconfig',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado em'),
        ),
        migrations.AddField(
            model_name='movimentoconfig',
            name='movement_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='data'),
        ),
        migrations.AddField(
            model_name='movimentoconfig',
            name='situacao',
            field=models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Avaliando'), ('4', 'Analise'), ('5', 'Paralizado'), ('6', 'Pendente'), ('7', 'Negado')], default=2, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='crm.person', verbose_name='user responsavel'),
        ),
    ]
