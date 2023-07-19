from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')

    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.nome


class Lancamento(models.Model):
    descricao = models.CharField(
        max_length=255, null=True, verbose_name='Descrição')
    data_lancamento = models.DateField(
        default=timezone.localdate, verbose_name='Data Lançamento')
    data_pagamento = models.DateField(
        default=timezone.localdate, verbose_name='Data Pagamento')
    valor = models.IntegerField(null=False, verbose_name='Valor')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)  # noqa E501
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)  # noqa E501
    nota = models.TextField(verbose_name='Notas')
    genero = models.CharField(
        max_length=1,
        choices=(
            ('D', 'Débito'),
            ('C', 'Crédito'),
        )
    )

    # Metodo magico str, permite sobreescrever 'qualquer coisa' - permite indentificar o lancamento # noqa E501

    class Meta:
        verbose_name = 'descrição'

    def __str__(self):
        return self.descricao
