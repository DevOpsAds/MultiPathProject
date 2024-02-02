from django.db import models


from app.models import (
    Address,
    Active,
    TimeStampedModel,
    RegisterCaledarTime,
    CreatedBy,
    RegisterCalendar,

)
from crm.models import MovimentoConfig
from expense.models import Spending, CustomizingSpend
from finance.models import CheckAccount, PaymentMethod,Imposto
from supplier.models import Supplier



# Direção de atuação do mercado 

class MarketCredate( Active,CreatedBy):

    market_classify = models.CharField('classificação de operação', max_length=50,  null=True, blank=True)
 



    spending = models.ForeignKey(
        Spending,
        on_delete=models.CASCADE,
        verbose_name='ramo',
        related_name='despesas',

    )


    classify = models.ForeignKey(
        CustomizingSpend,
        on_delete=models.CASCADE,
        verbose_name='classificação',
        related_name='item',
 
    )





    class Meta:
     ordering = ('market_classify',)
     verbose_name = 'classificação de mercado'
     verbose_name_plural = 'classificadores do mercado'

  

    def __str__(self):
        return str(self.marketd_classify)




# Direção de atuação do mercado 

