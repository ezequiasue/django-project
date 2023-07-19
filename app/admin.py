from django.contrib import admin

from app import models


@admin.register(models.Lancamento)
class Lancamento(admin.ModelAdmin):
    list_display = 'id', 'descricao', 'data_lancamento', 'data_pagamento', 'valor', 'genero', 'nota',  # noqa E501
    list_filter = 'descricao', 'data_lancamento',
    search_fields = 'id', 'descricao', 'data_lancamento', 'data_pagamento', 'valor',  # noqa E501
    list_editable = 'valor',
    list_per_page = 10


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'nome',
    list_filter = 'nome',
    search_fields = 'id', 'nome',
    list_per_page = 10
