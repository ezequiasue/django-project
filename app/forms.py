from django import forms
from .models import Lancamento


class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ['descricao', 'data_lancamento',
                  'data_pagamento', 'valor', 'categoria',
                  'autor', 'nota', 'genero']
