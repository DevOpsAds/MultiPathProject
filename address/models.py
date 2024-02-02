import uuid
from django.db import models
from django.contrib.auth.models import User

class UuidModel(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    
    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=False,
        auto_now=True,
        null=True, blank=True

    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True,
        null=True, blank=True

    )

    class Meta:
        abstract = True

class CreatedBy(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name='criado por',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,

    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class city(models.Model):

    MUNICIPALITY = (

    	('UF', 'Estado'),
        ('MG', 'Minas Gerais'),
        ('SP', 'São paulo'),
        ('RJ', 'Rio de Janeiros'),
        ('ES', 'Espirito Santo'),
    )

    name = models.CharField('cidade', max_length=100, null=True,
        blank=True)
    uf = models.CharField('UF', max_length=2, choices=MUNICIPALITY, null=True,
        blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'cidade'
        verbose_name_plural = 'cidades'
        

class distr(models.Model):
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


class VinCep(models.Model):
    tb_cep_vinculado = models.CharField('auto_', max_length=11,blank=True, null=True,)
    fk_tb_auto_vincu = models.CharField('fk_ resistro_vinculado', max_length=9,blank=True, null=True,)   

    cep = models.CharField('cep', max_length=9)
    endereco = models.CharField('logradouro', max_length=40)
    complement = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True

    )
    cidade = models.CharField('cidade', max_length=40)
    bairro = models.CharField('bairro', max_length=40)
    uf = models.CharField('uf', max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bairro

    class Meta:
        ordering = ('cep',)
        verbose_name = 'vinCep'
        verbose_name_plural = 'C_ viculados'
     



class Cep(models.Model):
    #twr1:p/solo
   
    cep = models.CharField('cep', max_length=9)
    endereco = models.CharField('logradouro', max_length=40)
    cidade = models.CharField('cidade', max_length=40)
    bairro = models.CharField('bairro', max_length=40)
    uf = models.CharField('uf', max_length=40)

    def __str__(self):
        return self.uf

    class Meta:
        ordering = ('cep',)
        verbose_name = '@) base de dados e endereços'
        verbose_name_plural = '@) base de dados endereços'




class Address(models.Model):  # classificaçao das rotinas



    MUNICIPALITY = (
        ('MG', 'Minas Gerais'),
        ('SP', 'São paulo'),
        ('RJ', 'Rio de Janeiros'),
        ('ES', 'Espirito Santo'),
    )

   
    uf = models.CharField('UF', max_length=2, choices=MUNICIPALITY,blank=True, null=True,)

       
    cep = models.ForeignKey(
        Cep,
        verbose_name='cep',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    city = models.ForeignKey(
        city,
        verbose_name='cidade',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    district = models.ForeignKey(
        distr,
        verbose_name='bairro',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    address= models.CharField('rua ', max_length=200, blank=True, null=True,)

    address_number=models.IntegerField('número', null=True, blank=True)

    complement = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True

    )

    STATUS = (
        ('texting', 'Texting'),
        ('creating', 'Creating'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    progress = models.CharField(
        max_length=8,
        choices=STATUS,
        blank=True, null=True,
    )


    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'address': self.address,
            'address_number': self.address_number,
            'complement': self.complement,
            'district': self.district,
            'city': self.city,
            'uf': self.uf,
            'cep': self.cep,

        }

