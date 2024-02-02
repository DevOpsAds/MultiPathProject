from django.db import models
from django.urls import reverse_lazy

from app.models import (
    Active,
    Address,
    Contact,
    Document,
    TimeStampedModel,
    UuidModel,
    Financial,
    CreatedBy,
    RegisterCalendar,
    GrupAcessFor,
    Profissional,
    base_name,
    CallMyMother,
    

)


class Person(UuidModel, TimeStampedModel, Address, Document, Active,RegisterCalendar ,GrupAcessFor,Contact,Profissional):



    first_name = models.CharField('nome pro', max_length=50, help_text='Digite somente o primeiro nome.')

    last_name = models.CharField('sobrenome', max_length=50, null=True, blank=True)  # noqa E501

    email = models.EmailField(null=True, blank=True)




    class Meta:
        ordering = ('first_name','cargo')
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'
    

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name or ""}'.strip()

    def get_absolute_url(self):
        return reverse_lazy('crm:person_detail', kwargs={'pk': self.pk})

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'cargo':self.cargo,

        }

    def to_dict_base(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'cargo':self.cargo,
        }

    def __str__(self):
        return str(self.full_name)

class Photo(models.Model):

    fk_matrix = models.ForeignKey(
        CallMyMother,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Entre com fotos',
        related_name='fk_matrix_fotos',)

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='foto',
        related_name='photos',
    )

    photo = models.ImageField('foto', upload_to='')

    class Meta:
        ordering = ('pk',)
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return str(self.person)


class Routine(GrupAcessFor,Active,CreatedBy,RegisterCalendar,TimeStampedModel): #classificaçao das rotinas
    #classifique a quanto finaceiras ou outras 

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='user responsavel',
        related_name='users',
    )

    modulo = models.CharField(max_length=255)

    STATUS = (
        ('1', 'Testando'),
        ('2', 'Criando'),
        ('3', 'Negada'),
        ('4', 'Valendo'),
    )

    progress = models.CharField(
        max_length=8,
        choices=STATUS,
    )

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('modulo','pk','person')
        verbose_name = 'rotina'
        verbose_name_plural = 'routines'

    def __str__(self):
        return str(self.modulo)


class MovimentoConfig(GrupAcessFor,Active,CreatedBy,RegisterCalendar): # Configuração de movimentos contabeis
    #caracteriza melhor aind a obijetivo do trato da rotina caso for financeira tratar de alimentação , ou caso gastos com combustiveis 
    #acredito ser um bom modo para permiti coneção com com o fornecdor mais pretendo classificar o estabelcimento primeiro 


    routine = models.ForeignKey(
        Routine,
        on_delete=models.CASCADE,
        verbose_name='routine',
        related_name='routines',
    )

    name_conf = models.CharField('nome', max_length=255)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ('routine',)
      verbose_name = 'Movimento_conf.'
      verbose_name_plural = 'Movimentos_conf.'


    @property
    def routine_moviment(self):
        return f' {self.routine or ""  } {str("/->")} {self.name_conf }'.strip()

    def __str__(self):
       return str(self.routine_moviment)


class Payment_methods(models.Model): # Configuração de movimentos contabeis
    #esse metodo ainda nao teve toda minha atenção porem confira o intersse de registrar aqui metodos de pagamento cartao ou outros acho que 
    #foi descontinuado e deve estar em outra area do sistema 

    name = models.CharField('nome', max_length=255)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
      ordering = ('pk',)
      verbose_name = 'finace.'
      verbose_name_plural = 'finaces!x ? crm.'


    @property
    def descriptio_lance(self):
        return f' {self.carteira or ""  } {str("/->")} {self.nuber_doc }'.strip()

    def __str__(self):
       return str(self.descriptio_lance)


class Unit(CallMyMother,):  #twr 1:p/solo    
   
    index=models.IntegerField('indíce', null=True, blank=True)
    unidade = models.CharField('nome/unidade', max_length=70)
    descricao = models.CharField('uso p', max_length=150,null=True, blank=True )

    class Meta:
        ordering = ('index','unidade',)
        verbose_name = 'Criar grandeza'
        verbose_name_plural = 'Criar grandezas'

    def __str__(self):
        return str(self.unidade)
    #so E PERIMITIDO CRIAR DIPLAI LINK ENTRE CAMPOS COM O MESMO NOME INDEX E INDEX OUTROS CAMPOS 



'''
    class Finaces(Financial):  # Configuração de movimentos contabeis

        Movemtent_config = models.ForeignKey(
            MovimentoConfig,
            on_delete=models.CASCADE,
            verbose_name='Movimento_cont',
            related_name='Movimentos_conf',
        )

        created_at = models.DateTimeField(auto_now_add=True)

        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ('pk',)
            verbose_name = 'finace.'
            verbose_name_plural = 'finaces.'

        @property
        def descriptio_lance(self):
            return f' {self.carteira or ""} {str("/->")} {self.nuber_doc}'.strip()

        def __str__(self):
            return str(self.descriptio_lance)
'''