from django.contrib.auth.models import User
from django.db import models
from eleutero.models import Fl1,Step_1,Step_2
from expense.models import CustomizingSpend
from app.models import (
    Active,
    Address,
    Document,
    TimeStampedModel,
    UuidModel,
    Financial,
    CreatedBy,
    RegisterCalendar,
    RegisterCaledarTime,
    GrupAcessFor,
    Regions

)


# Lockwell_land repace: status testing models .ok
#CustomizingSpend
class Fl2_Fl1(GrupAcessFor,Active,CreatedBy,RegisterCalendar,TimeStampedModel):#twr1:p/solo #classificaçao das rotinas

    fl2_evento_permitido = models.ForeignKey(
        Fl1,
        on_delete=models.CASCADE,
        verbose_name='caso',
        related_name='fl1_matrix')
    matx_name = models.CharField('insira um titulo', max_length=150)
    description = models.TextField('descreva',max_length=255,help_text="Resumo de até 220* caracteres")
    created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,blank=True)


    class Meta:
        ordering = ('matx_name','fl2_evento_permitido')
        verbose_name = 'Qualifique o caso'
        verbose_name_plural = 'Qualifique os casos '
    def __str__(self):
        return str(self.matx_name)


class Fl2_Step_1(GrupAcessFor,Active,CreatedBy,TimeStampedModel,RegisterCaledarTime): #classificaçao das rotinas
    
    step_number=models.IntegerField('informe o movimento', null=True, blank=True)
    Fl2_passo = models.ForeignKey(
        Step_1,
        on_delete=models.CASCADE,
        verbose_name='evidências',
        related_name='Fl2_passo') 
    command_fl1 = models.ForeignKey(
        Fl2_Fl1,
        on_delete=models.CASCADE,
        verbose_name='movimentos',
        related_name='matrix',)
    name_step_listar = models.CharField('insira um titulo', max_length=100,help_text='Insira um titulo que melhor expresse o problema a ser tratado' )
    STATUS = (
        ('1', 'Esperando'),
        ('2', 'Atrasado'),
        ('3', 'problema'),
        ('4', 'Preparando'),)
    progress = models.CharField('reporte andamento',
        max_length=10,
        choices=STATUS,)
    description = models.TextField('descreva',max_length=255,help_text= "Resuma em 255* caracteres")
    created_user= models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True)

    class Meta:
        ordering = ('step_number','command_fl1')
        verbose_name = 'especifique a qualificação'
        verbose_name_plural = 'especifique as qualificações'

    @property
    def sub_list_matrix(self):
        return f' {self.command_fl1 or ""} {str("/->")} {self.name_step_listar}'.strip()

    def __str__(self):
        return str(self.sub_list_matrix)


class Fl2_Step_2 (GrupAcessFor,Active,CreatedBy,TimeStampedModel,RegisterCaledarTime): #classificaçao das rotinas

    step_number=models.IntegerField('nº',null=True,blank=True)
    Fl2_type_item = models.ForeignKey(
        Step_2,
        on_delete=models.CASCADE,
        verbose_name='indentifique',
        related_name='Fl2_matrix')
    step = models.ForeignKey(
		Fl2_Step_1,
		on_delete=models.CASCADE,
		verbose_name='execulte',
		related_name='matrix',)
    item_name = models.CharField('insira um titulo',max_length=100,null=True,blank=True)
    type_item = models.CharField('subtitulo',max_length=100,null=True,blank=True)
    STATUS = (
        ('1', 'Esperando'),
        ('2', 'Atrasado'),
        ('3', 'problema'),
        ('4', 'Preparando'),)
    progress = models.CharField('informe o andamento',
        max_length=10,
        choices=STATUS,)


    class Meta:
        ordering = ('step','step_number',)
        verbose_name = 'criar objetivo'
        verbose_name_plural = 'criar objetivos '



    def __str__(self):
        return str(self.item_name)









