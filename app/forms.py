from django.views import forms
from django.shortcuts import FormHelper, Layout, Submit
from django.contrib import messages
from .models import *
from django.views import View
from django.contrib import messages



class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'titulo',
            'autor',
            'editora',
            'genero',
            'preco',
            'data_plub',
            'status',
            Submit('submit', 'Salvar')
)
