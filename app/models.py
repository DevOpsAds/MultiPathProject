import uuid
from django.contrib.auth.models import User,Group
from django.db import models
from django.utils.timezone import now



#from localflavor.br.br_states import STATE_CHOICES


class UuidModel(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True

class Profissional(models.Model):
    nome = models.CharField( max_length=100, null=True, blank=True)
    cargo = models.CharField( max_length=20, null=True, blank=True)
    referenciais = models.TextField('Referncia / assuntos', null=True, blank=True)
    
    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'nome': self.nome,
            'cargo': self.cargo,
            'referenciais': self.referenciais,

        }



class Contact(models.Model):
    
    REDE_SOCIAL_CHOICES =(
        ('Facebook','Facebook'),
        ('Twitter','Twitter'),
        ('Instagram','Instagram'),
        ('Linkedin','Linkedin'), 
        ('Outro','Outro'),
    )

    CANAL_VENDAS_CHOICES =(
        ('Telefone','Telefone'),
        ('E-mail','E-mail'),
        ('Whatsapp','Whatsapp'),
        ('Presencial','Presencial'), 
        ('Outro','Outro'),
    )


    nome = models.CharField( max_length=100, null=True, blank=True)
    cargo = models.CharField( max_length=20, null=True, blank=True)
    telefone = models.CharField( max_length=20, null=True, blank=True)
    email = models.EmailField( null=True, blank=True)


    rede_social = models.CharField(
        max_length=20,
        choices=REDE_SOCIAL_CHOICES,
        null=True, blank=True
    )

    canal_vendas = models.CharField(
       max_length=20,
        choices=CANAL_VENDAS_CHOICES,
        null=True, blank=True
    )
    
    interesses = models.TextField('Intersses / Informes', null=True, blank=True)
    

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'nome': self.nome,
            'cargo': self.cargo,
            'telefone': self.telefone,
            'email': self.email,
            'rede_social': self.rede_social,
            'canal_vendas': self.canal_vendas,
            'interesses': self.interesses,
            

        }


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=False,
        auto_now=True

    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True

    )

    class Meta:
        abstract = True

class GrupAcessFor(models.Model):
    grup = models.ForeignKey(
        Group,
        verbose_name='Acessível para grup',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )
  

    class Meta:
        abstract = True

    def to_dict_base(self):
        
        return {
            'grup': self.grup

        }


class CreatedBy(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name='privilegio',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def to_dict_base(self):
        
        return {
            'created_by': self.created_by

        }


class Address(models.Model):
    address = models.CharField(
        'endereço',
        max_length=100,
        null=True,
        blank=True

    )

    address_number = models.IntegerField('número', null=True, blank=True)

    complement = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True

    )

    district = models.CharField(
        'bairro',
        max_length=100,
        null=True,
        blank=True

    )

    city = models.CharField('cidade', max_length=100, null=True, blank=True)

    uf = models.CharField(
        'UF',
        max_length=2,
       # choices=STATE_CHOICES,
        null=True,
        blank=True

    )

    cep = models.CharField('CEP', max_length=9, null=True, blank=True)

    country = models.CharField(
        'país',
        max_length=50,
        default='Brasil',
        null=True,
        blank=True

    )
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


class Document(models.Model):
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True,
        null=True,
        blank=True

    )

    rg = models.CharField('RG', max_length=11, null=True, blank=True)

    cnh = models.CharField('CNH', max_length=20, null=True, blank=True)

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'cpf': self.cpf,
            'rg': self.rg,
            'cnh': self.cnh,

        }



class Active(models.Model):

    STATE_ACTIVE_CHOICES =(
        ('1','Aprovado'),
        ('2','Aguardando'),        
        ('3','Avaliando'),
        ('4','Analise'),
        ('5','Paralizado'),
        ('6','Pendente'),
        ('7','Negado'),  
        
    )


    situacao = models.CharField(
        max_length=20,
        default=2,
        choices=STATE_ACTIVE_CHOICES,
        null=True, blank=True
    )

    active = models.BooleanField('ativo', default=False)
    exist_deleted = models.BooleanField(
        'existe/deletado',
        default=True,
        help_text='Se for True o item existe. Se for False o item foi deletado.'

    )

    class Meta:
        abstract = True

    def to_dict_base(self):
        
        return {
            'situacao': self.situacao

        }
    





#finaceiros
class RegisterCalendar(models.Model):
    movement_date = models.DateField(
        'data', null=True, blank=True, default=now,
    )

    class Meta:
        abstract = True


class RegisterCaledarTime(models.Model):
    movement_date = models.DateTimeField(
        'data/hora', null=True, blank=True, default=now

    )

    class Meta:
        abstract = True


class Financial(models.Model):

    movement_date = models.DateField(
        'data', null=True, blank=True, default=now,
    )



    type_paygment = models.CharField('forma de pagamento', max_length=35, )

    nuber_doc = models.CharField('numero do documento', max_length=10, )

    carteira = models.CharField('Carteira',max_length=35)

    value_pay = models.DecimalField('valor',
    max_digits=10,
    decimal_places=2,

    )

    description = models.TextField()

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'movement_date': self.movement_date,
            'movimento_contabel': self.movimento_contabel,
            'type_paygment': self.type_paygment,
            'nuber_doc': self.nuber_doc,
            'carteira': self.carteira,
            'value_pay': self.value_pay,
            'description': self.description,

        }

#implementar os cep ainda nao foi feio deixo somente o esquelo no bd


class CEP(models.Model):
#não use esse cep use o do adress 
    CEP = models.CharField('cep', max_length=9, )
    enderco = models.CharField('endereço', max_length=250, )
    cidade = models.CharField('cidade', max_length=250, )
    bairro = models.CharField('bairro', max_length=250, )
    UF = models.CharField('UF', max_length=250, )
    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'CEP': self.CEP,
            'enderco': self.enderco,
            'cidade': self.cidade,
            'bairro': self.bairro,
            'UF': self.UF,

        }

class CallMyMother(models.Model):
    call=models.IntegerField('call',null=True, blank=True)
    fk_matrix = models.BooleanField('Conect at matrix',default=True,help_text='Activated this process.')
    matrix_evolution = models.CharField('Object', max_length=255)
    
    class Meta:
        ordering = ('call','fk_matrix','matrix_evolution')
        verbose_name ='evolution'
        verbose_name_plural = '|__[Matrix]²£__|'
    def __str__(self):
        return str(self.matrix_evolution)  


class CallExpenseEleutero1vagao(models.Model):
    call=models.IntegerField('call',null=True, blank=True)
    fk_matrix = models.BooleanField('Conect at matrix',default=True,help_text='Activated this process.')
    matrix_evolution = models.CharField('Object', max_length=255)
    
    class Meta:
        ordering = ('call','fk_matrix','matrix_evolution')
        verbose_name ='evolution'
        verbose_name_plural = '|__[Matrix]²£_vg 1/_|'
    def __str__(self):
        return str(self.matrix_evolution)   




class Regions(models.Model):

    fk_matrix = models.ForeignKey(
        CallMyMother,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Entre com uma regional',
        related_name='fk_matrix_regional',)

    region = models.CharField('region', max_length=9, )

    description = models.CharField('desc', max_length=150, )
    STATUS = (
        ('texting', 'Texting'),
        ('creating', 'Creating'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    progress = models.CharField(
        
        max_length=8,
        choices=STATUS,
    )


    class Meta:
      ordering = ('region',)
      verbose_name = 'region'
      verbose_name_plural = 'reginales'



    def __str__(self):
       return str(self.region)

class base_name(models.Model):  #twr1:p/solo
   
   index=models.IntegerField('indíce', null=True, blank=True)

   name = models.CharField('nome/unidade...', max_length=70,null=True, blank=True )

   description = models.CharField('uso p.:', max_length=150,null=True, blank=True )



   class Meta:
    ordering = ('index','name',)
    verbose_name = 'A) Criar unidade'
    verbose_name_plural = 'A) Criar medidas e unidades'

    def __init__(self,index,name,description,other):
        self.name=name 
        self.index=index

    def __str__(self):
        return str(self.name)  


class base_name_Create(models.Model):

    index=models.IntegerField('indíce', null=True, blank=True)

    abreviacao = models.CharField('abreviação', max_length=150,null=True, blank=True )

    name = models.CharField('nome/unidade...', max_length=50,null=True, blank=True )

    description = models.CharField('uso p.:', max_length=150,null=True, blank=True )


    base_nome_grup = models.ForeignKey(
        base_name,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='indice de grupos',
        related_name='indice_base_name',
    )



    fase_principal = models.BooleanField(
        'fase/principal',
        default=False,
        help_text='Marque se. Esta é uma referência principal de grandeza.'

    )



    class Meta:
      ordering = ('base_nome_grup','index','pk')
      verbose_name = 'B) Criar Sub Titulo'
      verbose_name_plural = 'B) Criar Sub Titulos'

       
  
    def __str__(self):
        return str(self.abreviacao)     

class name_base_Convert(models.Model):

    
    index=models.IntegerField('indíce', null=True, blank=True)   

    function_name = models.CharField('nome de função ', max_length=50, help_text='Caso tenha. Digite o codyname_espec_functions.',) 

    base_nome_grup = models.ForeignKey(
        base_name,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='indice',
        related_name='indice_grup',
    )

    name = models.ManyToManyField(
        base_name_Create,
        verbose_name='apresentado',
        related_name='name_base1',
    )

    value_ref_int = models.IntegerField('valor ref.', help_text='Caso tenha. Digite o valor de referencia para operação da função.', null=True, blank=True) 




  

    class Meta:
      ordering = ('base_nome_grup','function_name','index','pk',)
      verbose_name ='C) Criar cobinação'
      verbose_name_plural = 'C) Criar cobinações'


    def __str__(self):
        return str(self.function_name)



class grandeza(CallMyMother):  #twr1:p/solo
    
   
    index=models.IntegerField('indíce', null=True, blank=True)
    unidade = models.CharField('nome/unidade', max_length=70)
    description = models.CharField('uso p', max_length=150,null=True, blank=True )

    class Meta:
        ordering = ('index','unidade',)
        verbose_name = 'Criar grandeza'
        verbose_name_plural = 'Criar grandezas'

    def __str__(self):
        return str(self.unidade)
    #so E PERIMITIDO CRIAR DIPLAI LINK ENTRE CAMPOS COM O MESMO NOME INDEX E INDEX OUTROS CAMPOS PODEM SER USADOS NORMALMENTOE
    #BASTAR SER HEDEIRO DE UMA FORING KEY ASSIM GRANDEZA PODE INVOCAR SEUS FILHOS CLASSES 
class Qualificar(CallMyMother):#twr1:p/sol

    index=models.IntegerField('indíce', null=True, blank=True)
    abreviacao = models.CharField('abreviação', max_length=150 )
    name = models.CharField('nome/unidade...', max_length=50,null=True, blank=True )
    description = models.CharField('uso p.:', max_length=150,null=True, blank=True )
    fk_grandeza = models.ForeignKey(
        grandeza,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='qualificar grandeza',
        related_name='grandeza_fk',)
    fase_principal = models.BooleanField(
        'principal/fase',
        default=False,
        help_text='Marque se. Esta é uma referência principal de grandeza.')
    
    class Meta:
      ordering = ('fk_grandeza','index','pk')
      verbose_name = 'qualificador'
      verbose_name_plural = 'qualificador de grandezas'

    def __str__(self):
        return str(self.abreviacao)   








