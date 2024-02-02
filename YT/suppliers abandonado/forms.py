from django import forms
from django.db.models import Q
from django.contrib.postgres.forms.ranges import RangeWidget, DateTimeRangeField
from suppliers.models import tb_fornecedor
from app.models import Regions
from relacionChip.models import Mineralandia,City,District
from collections import Counter



class SuppliersAll(forms.ModelForm):


    class Meta:
        model = tb_fornecedor
        fields = ('__all__')

        

    def __init__(self,cep=None, *args, **kwargs):
     super(SuppliersAll, self).__init__(*args, **kwargs)
     self.fields['cep'].widget.attrs['class'] = 'cep'
 
   
class Suppliers_complet_endereco_cad_use_updade(forms.Form):

    address_number=forms.IntegerField(label='nº', required=False)

    complemento=forms.CharField(label='complemeto',required=False)

    phone=forms.CharField(label='telefone', required=False)

    class Meta:
      
         fields = ('address_number','complemeto','phone')


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)



class Suppliers_sit_on_cad_use_updade(forms.ModelForm):

    STATUS = (
        ('texting', 'Texting'),
        ('creating', 'Creating'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )



    progress = forms.ChoiceField(
        choices=STATUS,
        required=False
    )



    exist_deleted = forms.BooleanField(
        label='em uso /inativo',
        help_text='Se for True para cadastro ativo(em uso) . Se for False o item está inativo.',
        required=False

    )

    
    class Meta:
         model = tb_fornecedor
         fields = ('progress','exist_deleted')

     
    def __init__(self, exist_deleted=None, progress=None,  *args, **kwargs):
        super().__init__(*args, **kwargs)


    
    




class Suppliers_flash(forms.ModelForm):

    trade_name = forms.CharField(label='nome fantasia ', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    social_name = forms.CharField(label='nome social ', required=True)
    cnpj = forms.CharField(label='cnpj',required=True)    
    email = forms.EmailField(label='email', required=False)



    bairro_list= tb_fornecedor.objects.values_list('bairro',flat=True)
    contador_bairros=Counter(bairro_list)
    bairros_opcoes=[(bairro, f"{bairro} ({contador})") for bairro,contador in contador_bairros.items()]

    bairro = forms.ChoiceField(
        choices=bairros_opcoes,
         required=False,    

    )

    
    class Meta:
         model = tb_fornecedor
         fields = ('trade_name','social_name','cnpj','email','bairro')

   

    def __init__(self, trade_name=None, social_name=None, cnpj=None,email=None,*args, **kwargs):
        super().__init__(*args, **kwargs)
        widget=forms.TextInput(attrs={'class':'form-control'})
    


       
    
class SuppliersForm0(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = tb_fornecedor
        fields = ('trade_name','social_name','progress','created_by')



class StateForm(forms.Form):

    STATE_CHOICES=(
        ('MG','Minas Gerais'),
        ('ES','Espirito Santo'),
        ('SP','São Paulo'),
        ('RJ','Rio de Janeiro'),
        ('PR','Paraná'),)
    
    state = forms.ChoiceField(
        choices=STATE_CHOICES,
        label='Estado',
        # widget=forms.Select(
        #     attrs={'class': 'form-control'}
        # )
    )    
    
    city = forms.ModelChoiceField(
            queryset=City.objects.none(),
            required=False
    )

    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        required=False

    )
    

    

    class Meta:
      
         fields = ('state','city','district')

   

    def __init__(self, state=None, city=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.filter(uf=state)
        if city:
         self.fields['district'].queryset = District.objects.filter(city=city)