from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Livro

#from django.views import View
#from django.shortcuts import FormHelper, Layout, Submit
#from django.contrib import messages
#from .models import Livro
#from django import forms

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'editora', 'genero', 'preco', 'data_plub', 'status']

    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'titulo',
            'autor',
            'editora',
            'genero',
            'preco',
            'data_pub',
            'status',
            Submit('submit', 'Salvar')
)
