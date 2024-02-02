from django.db import models
#from localflavor.br.br_states import STATE_CHOICES
from app.models import (
    Address,
    Active,
    TimeStampedModel,
    RegisterCaledarTime,
    CreatedBy,
    RegisterCalendar,

)

from supplier.models import Supplier,relchipSupplier


class Persona(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('telefone', max_length=15, null=True, blank=True)
    GENDER = (
        ('0', ''),
        ('man', 'homem'),
        ('woman', 'mulher'),
    )
    gender = models.CharField(
        'sexo',
        max_length=5,
        choices=GENDER,
        default='0'
    )
    district = models.ForeignKey(
        'District',
        verbose_name='bairro',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'gender': self.get_gender_display(),
        }


    exist_address = models.BooleanField(
        'em uso /inativo',
        default=False,
        help_text='Se for True o item ativo em uso . Se for False o item está inativo.'

    )


class City(models.Model):

    MUNICIPALITY = (
        ('MG', 'Minas Gerais'),
        ('SP', 'São paulo'),
        ('RJ', 'Rio de Janeiros'),
        ('ES', 'Espirito Santo'),
    )

    name = models.CharField('cidade', max_length=100)
    uf = models.CharField('UF', max_length=2, choices=MUNICIPALITY,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'cidade'
        verbose_name_plural = 'cidades'


class District(models.Model):
    name = models.CharField('distrito', max_length=100)
    city = models.ForeignKey(
        'City',
        verbose_name='cidade',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'bairro'
        verbose_name_plural = 'bairros'


# Create your models here.
class Cliente(models.Model):

	nome =models.CharField(max_length=30)

	def __str__(self):
		return self.nome


class Telefone(models.Model):
	
	numero=models.CharField(max_length=11,unique=True)

	cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
		
	def __str__(self):
		return self.numero	

class Mineralandia(models.Model):
	
	code =models.CharField(max_length=30)


	cliente=models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True )


	telefone=models.ForeignKey(Telefone, on_delete=models.SET_NULL, blank=True, null=True )
		
	def __str__(self):
		
		return self.code	


class Mineralandiafornecedor(models.Model):
	
	
	nome =models.CharField(max_length=30)

	usuario=models.ForeignKey(Telefone, on_delete=models.SET_NULL, blank=True, null=True, related_name='oneTokey',)
		
	def __str__(self):
		return self.nome	


