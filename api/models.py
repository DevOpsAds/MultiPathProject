from django.contrib.auth.models import User
from django.db import models

from address.models import Cep
from app.models import (CallExpenseEleutero1vagao,CallMyMother,grandeza,Active,Address,Document,TimeStampedModel,UuidModel,Financial,CreatedBy,RegisterCalendar,RegisterCaledarTime,GrupAcessFor,Regions,base_name,grandeza)
from fl2.models import Fl2_Step_2
from expense.models import Spending,CustomizingSpend
from crm.models import Person,Photo
from finance.models import Ca,Imposto,PaymentMethod


class CallApiQualification_grandezas_Person(models.Model):
    call=models.IntegerField('call',null=True, blank=True)

    fk_Person= models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='pessoa',
        related_name='un_fk_pessoa',
    )

    fk_matrix = models.BooleanField('Conect at matrix',default=True,help_text='Activated this process.')
    matrix_evolution = models.CharField('Object', max_length=255)
    
    class Meta:
        ordering = ('call','fk_matrix','matrix_evolution')
        verbose_name ='medida em pessoa'
        verbose_name_plural = 'MTX|medidas em pessoas'
    def __str__(self):
        return str(self.matrix_evolution)



class CallApiQualificationGrandezas (models.Model): #classificaçao das rotinas



    valor=models.FloatField('valor', null=True, blank=True,help_text='Entre com o valor coletado') 


    fk_qualify_person = models.ForeignKey(
        CallApiQualification_grandezas_Person,
        on_delete=models.CASCADE,
        verbose_name='qualificar pessoa',
        related_name='un_fk_qualificador_pessoa',
    )

    fk_grandeza = models.ForeignKey(
        grandeza,
        on_delete=models.CASCADE,
        verbose_name='Undade_medida',
        related_name='un_fk_grandeza',
    )

    fk_objeto_fl2 = models.ForeignKey(
        Fl2_Step_2,
        on_delete=models.CASCADE,
        verbose_name='Objeto',
        related_name='un_fk_criar_obje_fl2_step_2',
    )

    matx_name = models.CharField('nome', max_length=255)

    description = models.TextField(null=True)




    class Meta:
        ordering = ('matx_name',)
        verbose_name = 'dimensão e medida'
        verbose_name_plural = 'dimensões e medidas'

    def __str__(self):
        return str(self.matx_name)







