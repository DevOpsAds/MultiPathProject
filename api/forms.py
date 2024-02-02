from django import forms
#from django.db.models import Q
#from django.contrib.postgres.forms.ranges import RangeWidget, DateTimeRangeField
from .models import CallApiQualification_grandezas_Person,CallApiQualificationGrandezas
#from app.models import Regions
#from relacionChip.models import Mineralandia,City,District
#from collections import Counter



class ApiQualificPensonAll(forms.ModelForm):


    class Meta:
        model = CallApiQualification_grandezas_Person
        fields = ('__all__')

        

    def __init__(self, *args, **kwargs):
     super(ApiQualificPensonAll, self).__init__(*args, **kwargs)
    

class ApiGrandezaPerson(forms.ModelForm):


    class Meta:
        model = CallApiQualificationGrandezas
        fields = ('fk_qualify_person','fk_grandeza','fk_objeto_fl2','matx_name','description')
    
    def __str__(self):
        return f"{self.situacao}-{self.situacao_display()}"    


    def __init__(self, *args, **kwargs):
     super(ApiGrandezaPerson, self).__init__(*args, **kwargs)

   
 
   