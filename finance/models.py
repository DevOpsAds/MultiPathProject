from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from crm.models import MovimentoConfig

from app.models import (
    Active,
    Address,
    Document,
    TimeStampedModel,
    UuidModel,
    Financial,
    CreatedBy,
    RegisterCalendar,

)

from .payment_requirements.model_requeri_payments import(
BankModel,
PixModel,
moneyModel,

)
#classe para receber classificar carteiras de movimentação
"""
# - defina finance em classes;

# crie uma classe com as carteiras possiveis

# cada carteira devara ter um saldo movimentos

# tipo e descrição de uso.

 # Cada cartira possui, tipos de movimentão finaceire ea variação relativa de pagamentos,
 #    CONJUT: Class_ cach:
 #
 # a clace principal do pactote fica reponsavel por implementar todos os conjuntos em o universo finace
 """




class Ca (models.Model):#twr1:p/solo #defin o  nome de caixas  finaceiras_ check account -#uso restrict

    name = models.CharField('nome', max_length=50, help_text='Digite o nome da conta check account')
    description = models.TextField(max_length=255)
    created_by =models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
      ordering = ('name',)
      verbose_name = 'Criar conta para caixa'
      verbose_name_plural = 'Criar contas de caixas'

    def __str__(self):
       return str(self.name)



class PaymentMethod (models.Model):#twr1:p/solo #defin o formas possiveis de pagamentos de um modo geral para o sistema    name = models.CharField('nome', max_length=50, help_text='Digite o nome da conta')
    name= models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
      ordering = ('name',)
      verbose_name = 'Criar meio de pagamento'
      verbose_name_plural = 'Criar meios de pagamentos'
    def __str__(self):
       return str(self.name)



class CheckAccount(models.Model):

    bank = models.ForeignKey(
        Ca,
        on_delete=models.CASCADE,
        verbose_name='checkaccount',
        related_name='checkaccounts',

    )






class PrivilegesAccount (CheckAccount,UuidModel, Active,BankModel,PixModel,CreatedBy,Address,moneyModel): #defin o formas possiveis de pagamentos de um modo geral para o sistema    name = models.CharField('nome', max_length=50, help_text='Digite o nome da conta')



    def __str__(self):
       return str(self.bank)



class BalanceInitilAccount ( Active,CreatedBy,RegisterCalendar,TimeStampedModel,CheckAccount): #defin o formas possiveis de pagamentos de um modo geral para o sistema    name = models.CharField('nome', max_length=50, help_text='Digite o nome da conta')


    value_pay = models.DecimalField(
        'valor',
        max_digits=10,
        decimal_places=2,
    )


    def __str__(self):
       return str(self.bank)


class Imposto(Active,CreatedBy,RegisterCalendar,TimeStampedModel,CheckAccount):#twr1:p/solo #defin o formas possiveis de pagamentos de um modo geral para o sistema    name = models.CharField('nome', max_length=50, help_text='Digite o nome da conta')
    
    n_imposto = models.CharField('nome',max_length=20, null=True, blank=True, help_text='Digite o nome do imposto')
    description = models.TextField(max_length=100, null=True, blank=True)
    taxa = models.IntegerField('taxa %',
         validators=[MaxValueValidator(99)],
         null=True,
         blank=True)
    value_pay = models.DecimalField(
        'valor',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True)
    MovimentoConfig= models.ForeignKey(
        MovimentoConfig,
        on_delete=models.CASCADE,
        verbose_name='atender ao interesse',
        related_name='MovimentoConfig',
        null=True,
        blank=True)
    I_federal = models.DecimalField(
        'I.Federal',
        max_digits=10,
        decimal_places=2,
        null=False, blank=True)
    I_Estadual = models.DecimalField(
        'I.Estadual',
        max_digits=10,
        decimal_places=2,
        null=False, blank=True)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Criar um imposto'
        verbose_name_plural = 'Criar impostos'
    
    def __str__(self):
       return str(self.n_imposto)





