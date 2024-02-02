from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from address.models import Cep
from app.models import (CallExpenseEleutero1vagao,CallMyMother,Active,Address,Document,TimeStampedModel,UuidModel,Financial,CreatedBy,RegisterCalendar,RegisterCaledarTime,GrupAcessFor,Regions,base_name,grandeza)
from expense.models import Spending,CustomizingSpend
from crm.models import MovimentoConfig,Person,Photo
from finance.models import Ca,Imposto,PaymentMethod
from supplier.models import meterorologia

class Gn (GrupAcessFor,Active,CreatedBy,RegisterCalendar): #classificaçao das rotinas

    index=models.IntegerField('index l.', null=False, blank=False,help_text="linha ..")
    coluna=models.CharField('col.', max_length=15,help_text="coluna ..")
    call=models.IntegerField('call', null=False, blank=False,help_text="piso ..")
    txt_name = models.CharField('nome', max_length=150)
    txt_referncial = models.CharField('ref./*', max_length=15, null=True, blank=True,)
    mem_description = models.TextField('descreva',null=True, blank=True,)

    registro_meterorologia = models.ForeignKey(
        meterorologia,
        on_delete=models.SET_NULL,
        verbose_name='Reg.met.',
        related_name='fk_in_met',
        null=True,
        blank=True
    )

    evento_permitido = models.ForeignKey(
        MovimentoConfig,
        on_delete=models.CASCADE,
        verbose_name='Mov.conf.',
        related_name='in_crm',
    )

    created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('call','index','coluna','txt_referncial','txt_name',)
        verbose_name = 'Gênesis'
        verbose_name_plural = 'Gênesis'

    def __str__(self):
        return str(self.txt_name)

class Gn_ceu_terra (GrupAcessFor,Active,CreatedBy,RegisterCalendar): #classificaçao das rotinas

    index=models.IntegerField('index l.', null=False, blank=False,help_text="linha ..")
    coluna=models.CharField('col.', max_length=15,help_text="coluna ..")
    call=models.IntegerField('call', null=False, blank=False,help_text="piso ..")
    txt_name = models.CharField('nome', max_length=150)
    txt_referncial = models.CharField('ref./*', max_length=15,null=True, blank=True,)
    mem_description = models.TextField('descreva',null=True, blank=True,)



    registro_meterorologia = models.ForeignKey(
        meterorologia,
        on_delete=models.SET_NULL,
        verbose_name='Reg.met.',
        related_name='fk_met',
        null=True,
        blank=True
    )

    evento_permitido = models.ForeignKey(
        Gn,
        on_delete=models.CASCADE,
        verbose_name='Gênesis.conf.',
        related_name='in_eleutero_gn',
    )
    created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('coluna','index','call','txt_referncial','txt_name',)
        verbose_name = 'A criação Céu Terra'
        verbose_name_plural = 'Criar um Protocolo'

    def __str__(self):
        return str(self.txt_name)


class Gn_luz (GrupAcessFor,Active,CreatedBy,RegisterCalendar): #classificaçao das rotinas

    index=models.IntegerField('index l.', null=False, blank=False,help_text="linha ..")
    coluna=models.CharField('col.', max_length=15,help_text="coluna ..")
    call=models.IntegerField('call', null=False, blank=False,help_text="piso ..")
    txt_name = models.CharField('nome', max_length=150)
    txt_referncial = models.CharField('ref./*', max_length=15,null=True, blank=True,)
    mem_description = models.TextField('descreva',null=True, blank=True,)

    registro_meterorologia = models.ForeignKey(
        meterorologia,
        on_delete=models.SET_NULL,
        verbose_name='Reg.met.',
        related_name='in_met',
        null=True,
        blank=True
    )

    evento_matrix = models.ForeignKey(
        Gn,
        on_delete=models.CASCADE,
        verbose_name='config_Gênesis..',
        related_name='GN_in_fk_matrix',
    )

    evento_permitido = models.ForeignKey(
        Gn_ceu_terra,
        on_delete=models.CASCADE,
        verbose_name='conf.Gênesis.',
        related_name='Fk_gn_in_eleutero',
    )
    created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('situacao','coluna','index','call','evento_permitido','txt_referncial','txt_name',)
        verbose_name = 'A luz'
        verbose_name_plural = 'Aplicar o protocolo'

    def __str__(self):
        return str(self.txt_name)


class Gn_noite (GrupAcessFor,Active,CreatedBy): #classificaçao das rotinas


    inicio_date = models.DateTimeField(
        'início/comerço', null=True, blank=True, default=now,help_text='data/hora')
    fim_date = models.DateTimeField(
        'fim/termino', null=True, blank=True, default=now,help_text='data/hora')


    index=models.IntegerField('index l.', null=False, blank=False,help_text="linha ..")
    coluna=models.CharField('col.', max_length=15,help_text="coluna ..")
    call=models.IntegerField('call', null=False, blank=False,help_text="piso ..")
    txt_name = models.CharField('nome', max_length=150)
    txt_referncial = models.CharField('ref./*', max_length=15,null=True, blank=True,)
    mem_description = models.TextField('descreva',null=True, blank=True,)



    registro_meterorologia = models.ForeignKey(
        meterorologia,
        on_delete=models.SET_NULL,
        verbose_name='Reg.met.',
        related_name='fk_at_met',
        null=True,
        blank=True
    )


    evento_matrix = models.ForeignKey(
        Gn,
        on_delete=models.CASCADE,
        verbose_name='config_Gênesis..',
        related_name='fk_GN',
    )

    evento_detalhadi = models.ForeignKey(
        Gn_ceu_terra,
        on_delete=models.CASCADE,
        verbose_name='conf.evento.',
        related_name='eleutero_fk_detalhado',
    )

    evento_permitido = models.ForeignKey(
        Gn_luz,
        on_delete=models.CASCADE,
        verbose_name='conf.detalhado em evento.',
        related_name='_in_eleutero_fk_fk',
    )
    created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('inicio_date','fim_date','situacao','coluna','index','call','evento_permitido','txt_referncial','txt_name',)
        verbose_name = 'A Noite'
        verbose_name_plural = 'atividade de protocolo registrados horarios e detalhes'

    def __str__(self):
        return str(self.txt_name)

class Fl1 (GrupAcessFor,Active,CreatedBy,RegisterCalendar,TimeStampedModel): #classificaçao das rotinas



    evento_permitido = models.ForeignKey(
        CustomizingSpend,
        on_delete=models.CASCADE,
        verbose_name='Movimento configurado',
        related_name='expense',
    )

    matx_name = models.CharField('nome', max_length=255)

    description = models.TextField()



    created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('matx_name','evento_permitido')
        verbose_name = 'matrix'
        verbose_name_plural = 'matrices'

    def __str__(self):
        return str(self.matx_name)

class Step_1 (GrupAcessFor,Active,CreatedBy,TimeStampedModel,RegisterCaledarTime): #classificaçao das rotinas
    
    step_number=models.IntegerField('passo', null=True, blank=True)

    fk_matrix = models.ForeignKey(
        CallExpenseEleutero1vagao,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Modularizado em call Expe...Eleutero...vg1',
        related_name='fk_matrix_eleutero',)

    command_fl1 = models.ForeignKey(
        Fl1,
        on_delete=models.CASCADE,
        verbose_name='autorizador',
        related_name='matrix',
    )

    name_step_listar = models.CharField('listar', max_length=100)

    STATUS = (
        ('1', 'Esperando'),
        ('2', 'Atrasado'),
        ('3', 'problema'),
        ('4', 'Preparando'),
    )

    progress = models.CharField(
        max_length=10,
        choices=STATUS,
    )

    description = models.TextField()



    created_user= models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('step_number','command_fl1')
        verbose_name = 'matrix 1'
        verbose_name_plural = ' passo'

    @property
    def sub_list_matrix(self):
        return f' {self.command_fl1 or ""} {str("/->")} {self.name_step_listar}'.strip()

    def __str__(self):
        return str(self.sub_list_matrix)


class Step_2 (Fl1,GrupAcessFor,Active,CreatedBy,TimeStampedModel,RegisterCaledarTime): #classificaçao das rotinas

	step_number=models.IntegerField('passo', null=True, blank=True)
    


	step = models.ForeignKey(
		Step_1,
		on_delete=models.CASCADE,
		verbose_name='tarf',
		related_name='matrix',
    )

	item_name = models.CharField('nome', max_length=100)
    
	type_item = models.CharField('tipo', max_length=100)

	STATUS = (
		('1', 'Esperando'),
		('2', 'Atrasado'),
		('3', 'problema'),
		('4', 'Preparando'),
	)


	progress = models.CharField(
		max_length=10,
		choices=STATUS,
	)


	class Meta:
		ordering = ('step','step_number',)
		verbose_name = 'items'
		verbose_name_plural = 'create_my_itens'

	@property
	def itens_list_create(self):
		return f' {self.step or ""} {str("/->")} {self.item_name}'.strip()

	def __str__(self):
		return str(self.type_item)

##ter 22  agosto  2023 repaginação do eleutero
##quart 23 aplicando classe externas

class StartCalendar(models.Model):
    movement_date = models.DateField(
        'Registro de início', null=True, blank=True,
    )

    class Meta:
        abstract = True

class SendBigData (StartCalendar,GrupAcessFor,Active,CreatedBy): #classificaçao das rotinas
#twr1:p/solo * eliminar 

    fk_gradeza = models.ForeignKey(
        grandeza,
        on_delete=models.CASCADE,
        help_text='Para Registros de unidades de medidas na base em sistema @admin',
        verbose_name='Registro de Medidas',
        related_name='fk_big_gradeza')

    
    fk_cep = models.BooleanField('criar a enderços',default=False,help_text='Para habiliter neste processo.')
    index=models.IntegerField('nº',)

    description = models.TextField('descreva',help_text='Resuma em 300* caracteres.')
    created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True)

    class Meta:
        ordering = ('index',)
        verbose_name = 'CALL: my mother now'

    def __str__(self):
        return str(self.matrix_evolution)


class ctrlSolo_Gr (GrupAcessFor,Active,CreatedBy): #classificaçao das rotinas
#twr1:p/solo *eliminador desconectar com viculo com tabela grandeza em adimni


    fk_gradeza = models.ForeignKey(
        grandeza,
        on_delete=models.CASCADE,
        null=True,
        help_text='Para Registros de unidades de medidas na base em sistema @admin',
        verbose_name='Registro de Medidas',
        related_name='fk_gradeza')

    fk_base_name = models.ForeignKey(
        base_name,
        on_delete=models.CASCADE,
        null=True,
        help_text='Para Registros de grandezas na base em sistema @admin',
        verbose_name='Registro de unidades',
        related_name='fk_app')
    fk_person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,
        help_text='Para Registros de pessoas e profissionais em base em sistema ...',
        verbose_name='Registro de pessoas',
        related_name='fk_app')
    fk_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=True,
        help_text='Para Registros de imagens na base em ...',
        verbose_name='Registro de imagens',
        related_name='fk_photo')
    fk_spending= models.ForeignKey(
        Spending,
        on_delete=models.CASCADE,
        null=True,
        help_text='Para Registros de despesas e tratamentos em ... @admin',
        verbose_name='Registro de despesas',
        related_name='fk_spending')
    fk_ca= models.ForeignKey(
        Ca,
        on_delete=models.CASCADE,
        null=True,
        help_text='Para Registros de contas de caixa ... @admin',
        verbose_name='Registro de contas',
        related_name='fk_ca')
    fk_imposto= models.ForeignKey(
        Imposto,
        on_delete=models.CASCADE,
        null=True,
        help_text='Para Registros de impostos em contas de caixa ... @admin',
        verbose_name='Registro de impostos',
        related_name='fk_imposto')
    fk_paymentmethod= models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        null=True,
        help_text='Para Registros de tipos propriedades de pagamentos contas de caixa (dinheiro, cartão ...).',
        verbose_name='Registro de prop. pagamentos',
        related_name='fk_paymentmethod')



    
    fk_cep = models.BooleanField('criar a enderços',default=False,help_text='Para habiliter neste processo.')
    index=models.IntegerField('nº', null=True, blank=True)
    matrix_evolution = models.CharField('Objeto', max_length=255)
    description = models.TextField('descreva',help_text='Resuma em 300* caracteres.')
    created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True)

    class Meta:
        ordering = ('index','matrix_evolution',)
        verbose_name = 'Criar objeto'
        verbose_name_plural = 'Criar objetos'

    def __str__(self):
        return str(self.matrix_evolution)
'''       

class Step_1 (GrupAcessFor,Active,CreatedBy,TimeStampedModel,RegisterCaledarTime): #classificaçao das rotinas
    
    step_number=models.IntegerField('passo', null=True, blank=True)

    command_fl1 = models.ForeignKey(
        Fl1,
        on_delete=models.CASCADE,
        verbose_name='autorizador',
        related_name='matrix',
    )

    name_step_listar = models.CharField('listar', max_length=100)

    STATUS = (
        ('1', 'Esperando'),
        ('2', 'Atrasado'),
        ('3', 'problema'),
        ('4', 'Preparando'),
    )

    progress = models.CharField(
        max_length=10,
        choices=STATUS,
    )

    description = models.TextField()



    created_user= models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('step_number','command_fl1')
        verbose_name = 'matrix 1'
        verbose_name_plural = ' passo'

    @property
    def sub_list_matrix(self):
        return f' {self.command_fl1 or ""} {str("/->")} {self.name_step_listar}'.strip()

    def __str__(self):
        return str(self.sub_list_matrix)


class Step_2 (Fl1,GrupAcessFor,Active,CreatedBy,TimeStampedModel,RegisterCaledarTime): #classificaçao das rotinas

    step_number=models.IntegerField('passo', null=True, blank=True)
    


    step = models.ForeignKey(
        Step_1,
        on_delete=models.CASCADE,
        verbose_name='tarf',
        related_name='matrix',
    )

    item_name = models.CharField('nome', max_length=100)
    
    type_item = models.CharField('tipo', max_length=100)

    STATUS = (
        ('1', 'Esperando'),
        ('2', 'Atrasado'),
        ('3', 'problema'),
        ('4', 'Preparando'),
    )


    progress = models.CharField(
        max_length=10,
        choices=STATUS,
    )


    class Meta:
        ordering = ('step','step_number',)
        verbose_name = 'items'
        verbose_name_plural = 'create_my_itens'

    @property
    def itens_list_create(self):
        return f' {self.step or ""} {str("/->")} {self.item_name}'.strip()

    def __str__(self):
        return str(self.type_item)

'''







