from django.db import models



from app.models import (
    Address,
    Active,
    TimeStampedModel,
    RegisterCaledarTime,
    CreatedBy,
    RegisterCalendar,
)

from crm.models import MovimentoConfig,Photo
from expense.models import Spending, CustomizingSpend
from finance.models import CheckAccount, PaymentMethod,Imposto
from supplier.models import Supplier

from relacionChip.models import Mineralandiafornecedor

# Direção de atuação do mercado 

class MarketingCreate( Active,CreatedBy,TimeStampedModel):

	market_classify = models.CharField('Titulo para o mercado', max_length=50,  null=True, blank=True)
 



	spending_market= models.ForeignKey(
		Spending,
		on_delete=models.CASCADE,
		verbose_name='tratamento de despesa',
		related_name='spending_fk',
	)


	classify_market = models.ForeignKey(
		CustomizingSpend,
		on_delete=models.CASCADE,
		verbose_name='personalisão das despesas',
		related_name='CustomizingSpend',
	)


	class Meta:
		ordering = ('market_classify',)
		verbose_name = 'Crie um mercado'
		verbose_name_plural = '+ Criar mercados'

  

	def __str__(self):
		return str(self.spending_market)



# Direção de atuação do mercado 
class MarketingAddSuppliers( Active,CreatedBy,TimeStampedModel):



    
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='fornecedor',
        related_name='supplier',
    )

    marketingcreate = models.ForeignKey(
        MarketingCreate,
        on_delete=models.CASCADE,
        verbose_name='supplier market',
        related_name='marketingcreate',
    )    

    class Meta:
        ordering = ('marketingcreate',)
        verbose_name = 'map de mercado'
        verbose_name_plural = 'mercado em maps'

  

    def __str__(self):
        return str(self.supplier)

