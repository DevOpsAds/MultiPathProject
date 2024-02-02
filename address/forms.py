from django import forms
from django.contrib.postgres.forms.ranges import RangeWidget, DateTimeRangeField
from .models import Address,city,distr,Cep,VinCep
from relacionChip.models import Mineralandia,City,District


class MyCep_Form(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = VinCep
        fields = '__all__'
    
    def __init__(self, state=None, cep=None, bairro=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bairro'].queryset = VinCep.objects.filter(cep=cep)


class Ltext_Form(forms.ModelForm):
    required_css_class = 'required'

    movement_date=forms.DateTimeField(
        label='Data/Time',
        widget=forms.DateTimeInput(
            attrs= {'type':'datetime-local',
            }),

    )

    class Meta:
        model = Cep
        fields = '__all__'


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

    
     
       

'''
 cep= forms.CharField(
         
             widget=forms.TextInput(attrs={'class':'form-control'})
            )


    class Meta:
        model = Cep
        fields = (
            'tb_cep_vinculado',
            'fk_tb_auto_vincu',
            'cep',
            'endereco',
            'bairro',
            'cidade',
            'uf'
          )
class LogChip_Form(forms.ModelForm):
    required_css_class = 'required'

    movement_date=forms.DateTimeField(
        label='Data/Time',
        widget=forms.DateTimeInput(
            attrs= {'type':'datetime-local',
            }),

    )

    class Meta:
        model = Mineralandia
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LogChip_Form, self).__init__(*args, **kwargs)
        for movement_date, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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
 
    




   
     




class LogMarket_Form(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = LogMarket
        fields = '__all__'

 

        widgets = {
            "datatimerange":RangeWidget(
                forms.SplitDateTimeWidget(
                    date_attrs={"type":"date"},
                    time_attrs={"type":"time"},
                ),
            )

        }

   
        fields = (
            'first_name',
            'last_name',
            'email',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
            'country',
            'cpf',
            'rg',
            'cnh',
            'active',
        )
   

    def __init__(self, *args, **kwargs):
        super(LogMarket_Form, self).__init__(*args, **kwargs)
        #self.fields['movement_date'].widget.attrs['data'] = 'd/m/Y'
        for nuberFiscal, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['active'].widget.attrs['class'] = None


class PersonForm0(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Person
        fields = ('first_name', 'last_name')


class PersonForm1(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Person
        fields = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(PersonForm1, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = ''
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PersonForm2(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(PersonForm2, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = ''
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class PersonPhotoForm (forms.ModelForm):
    required_css_class = 'required'
    photo = forms.ImageField(required=False)

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'photo')

    def __init__(self, *args, **kwargs):
        super(PersonPhotoForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = ''
        self.fields['photo'].widget.attrs['class'] = None
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
'''