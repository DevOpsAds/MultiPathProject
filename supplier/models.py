from django.contrib.auth.models import User
from django.db import models

from app.models import(
UuidModel,
CreatedBy,
GrupAcessFor,
Active,
Address,
TimeStampedModel,
Contact,
)

class meterorologia(models.Model):



	referencia= models.CharField('referencia-1', max_length=10,null=True, blank=True)
	coleta= models.CharField('coleta da infor ', max_length=70,default='met.decea.mil.br',null=True, blank=True)
	tipodoc= models.CharField('tipo de documento ', max_length=5,null=True, blank=True)
	diadocsis= models.IntegerField('dia da coleta do sistema',null=True, blank=True)
	horadocsis= models.CharField('hora da coleta da previsão', max_length=7,null=True, blank=True)

	coletainfo1= models.CharField('coleta info 1', max_length=10,null=True, blank=True)
	coletainfo2= models.CharField('coleta info 2', max_length=10,null=True, blank=True)
	coletainfo3= models.CharField('coleta info 3', max_length=10,null=True, blank=True)
	coletainfo4= models.CharField('coleta info 4', max_length=10,null=True, blank=True)
	coletainfo5= models.CharField('coleta info 5', max_length=10,null=True, blank=True)
	coletainfo6= models.CharField('coleta info 6', max_length=10,null=True, blank=True)
	coletainfo7= models.CharField('coleta info 7', max_length=10,null=True, blank=True)
	coletainfo8= models.CharField('coleta info 8', max_length=10,null=True, blank=True)
	coletainfo9= models.CharField('coleta info 9', max_length=10,null=True, blank=True)
	coletainfo10= models.CharField('coleta info 10', max_length=10,null=True, blank=True)
	coletainfo11= models.CharField('coleta info 11', max_length=10,null=True, blank=True)
	coletainfo12= models.CharField('coleta info 12', max_length=10,null=True, blank=True)
	coletainfo13= models.CharField('coleta info 13', max_length=10,null=True, blank=True)
	coletainfo14= models.CharField('coleta info 14', max_length=10,null=True, blank=True)  

	class Meta:
		ordering = ('-diadocsis','-pk',)
		verbose_name = 'meterorologia'
		verbose_name_plural = 'meteorologicas'
    

	def __str__(self):
		return str(self.diadocsis)

class Var_meteorologicas(Active):

	registro_meterorologia = models.ForeignKey(
        meterorologia,
        on_delete=models.SET_NULL,
        verbose_name='Reg.met.',
        related_name='index_met',
        null=True,
        blank=True
    )

	VAR_METERIOLOGICAS =(
        ('1','BECMG'),
        ('2','FM'),
    )


	canal_vendas = models.CharField(
		max_length=20,
		choices=VAR_METERIOLOGICAS,
		null=True, blank=True
	)
	coletainfo1= models.CharField('coleta info 1', max_length=10,null=True, blank=True)
	coletainfo2= models.CharField('coleta info 2', max_length=10,null=True, blank=True)
	coletainfo3= models.CharField('coleta info 3', max_length=10,null=True, blank=True)
	coletainfo4= models.CharField('coleta info 4', max_length=10,null=True, blank=True)
	coletainfo5= models.CharField('coleta info 5', max_length=10,null=True, blank=True)


	class Meta:
		ordering = ('-coletainfo1','-pk',)
		verbose_name = 'integre meterorologia'
		verbose_name_plural = 'integração meteorologicas'
    

	def __str__(self):
		return str(self.coletainfo1)






class relchipSupplier(UuidModel,CreatedBy,GrupAcessFor,Active,Address,TimeStampedModel,Contact):

    
	reltrade_name = models.CharField('Nome fantasia', max_length=200)
	relsocial_name = models.CharField('Nome social', max_length=200, null=True, blank=True)
	relcnpj = models.CharField('Cnpj',max_length=14, unique=True, null=True, blank=True)
	relie = models.CharField('Ei', max_length=11, unique=True, null=True, blank=True)

	class Meta:
		ordering = ('situacao','-active','exist_deleted','reltrade_name',)
		verbose_name = 'fornecedor'
		verbose_name_plural = 'fornecedores'
	

	def __str__(self):
		return f"{self.reltrade_name}-{self.get_situacao_display()}"



class Supplier(UuidModel,CreatedBy,GrupAcessFor,Active,Address,TimeStampedModel,Contact):

    
	trade_name = models.CharField('Nome fantasia', max_length=200)
	social_name = models.CharField('Nome social', max_length=200, null=True, blank=True)
	cnpj = models.CharField('Cnpj',max_length=14, unique=True, null=True, blank=True)
	ie = models.CharField('Ei', max_length=11, unique=True, null=True, blank=True)
	
	class Meta:
		ordering = ('situacao','-active','exist_deleted','trade_name',)
		verbose_name = 'fornecedor'
		verbose_name_plural = 'fornecedores'
	
	def __str__(self):
		return f"{self.trade_name}-{self.get_situacao_display()}" 
	   



