from django.db import models

from app.models import (
    Active,
    Address,
    Document,
    TimeStampedModel,
    UuidModel,
    Financial,
    CreatedBy,
    RegisterCalendar,
    GrupAcessFor,
    CallExpenseEleutero1vagao,

)
from crm.models import MovimentoConfig


# este modulod trata as propriendade de uma despesa as contas paga ou gastos tentando direcionar o foco do itens disponiveipara gastos garnte o onameneto de direcção da dispesasp por explo em alimentaçaõ

class Spending (GrupAcessFor,Active,CreatedBy,RegisterCalendar,TimeStampedModel):#twr1:p/solo

    fk_matrix = models.ForeignKey(
        CallExpenseEleutero1vagao,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Modularizado em call Expensend...vg1',
        related_name='fk_matrix_spending',)

    name= models.CharField('nome',max_length=100,help_text='Digite o nome para qualificar o tratamento da despesa criado')
    description = models.TextField('resumo em 200* caracteres',max_length=255)
    movement_expense = models.ForeignKey(
        MovimentoConfig,
        on_delete=models.CASCADE,
        verbose_name='Criar uma despesa em:',
        help_text='Selecione a despesa para receber o tratamento',
        related_name='movement_expense',)

    
    class Meta:
      ordering = ('movement_expense',)
      verbose_name = 'Criar tratamento de despesa'
      verbose_name_plural = 'Criar tratamentos para despesas'
    def __str__(self):
       return str(self.name)



class CustomizingSpend (GrupAcessFor,Active,CreatedBy,RegisterCalendar,TimeStampedModel):


    name= models.CharField('nome',max_length=100)

    scientific_name = models.CharField('nome cientifico',max_length=150)

    species_type= models.CharField('espécie ou tipo',max_length=100)


    spending_classify = models.ForeignKey(
        Spending,
        on_delete=models.CASCADE,
        verbose_name='classificação',
        related_name='spendigs',
      

    )


    class Meta:
      ordering = ('created_by','grup','spending_classify')
      verbose_name = 'item'
      verbose_name_plural = 'personalização das despesas'

    def __str__(self):
        return f"{self.name}"





