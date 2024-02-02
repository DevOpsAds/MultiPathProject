from django import forms
#from django.db.models import Q
#from django.contrib.postgres.forms.ranges import RangeWidget, DateTimeRangeField
from .models import Supplier
#from app.models import Regions
#from relacionChip.models import Mineralandia,City,District
#from collections import Counter



class SupplierAll(forms.ModelForm):


    class Meta:
        model = Supplier
        fields = ('__all__')

        

    def __init__(self, *args, **kwargs):
     super(SupplierAll, self).__init__(*args, **kwargs)
     self.fields['cep'].widget.attrs['class'] = 'cep'

class SupplierList(forms.ModelForm):


    class Meta:
        model = Supplier
        fields = ('trade_name','active','exist_deleted','situacao','cnpj')
    
    def __str__(self):
        return f"{self.situacao}-{self.situacao_display()}"    


    def __init__(self, *args, **kwargs):
     super(SupplierList, self).__init__(*args, **kwargs)

   
 
   