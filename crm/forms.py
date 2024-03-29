from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Person
        # fields = '__all__'
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
        super(PersonForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
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