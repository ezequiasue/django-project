from django.shortcuts import render, redirect, get_object_or_404
from app.models import Lancamento
from django.core.paginator import Paginator
from django.db.models import Q


# Dashboard
def dashboard(request):
    return render(request, 'app/dashboard.html')


# List of all available
def listall(request):
    # Neste caso estou a filtrar tudo ".all", mas poderia definir outros tipos de filtros # noqa E501
    lancamento = Lancamento.objects.all().order_by('id')

    paginator = Paginator(lancamento, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'site_title': 'Lista-Lancamentos'}

    return render(request, 'app/listall.html', context)


def lancamento(request, lancamento_id):
    # single_lancamento = Lancamento.objects.filter(pk=lancamento_id).first()
    single_lancamento = get_object_or_404(
        Lancamento, pk=lancamento_id,)

    site_title = f'{single_lancamento.descricao}'

    context = {
        'lancamento': single_lancamento,
        'site_title': site_title

    }

    return render(
        request,
        'app/single_lancamento.html',
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('app:listall')

    lancamento = Lancamento.objects \
        .filter(  # Através do Q posso pesquisar por varios campos
            Q(descricao__icontains=search_value) |
            Q(valor__icontains=search_value)

        )\
        .order_by('id')

    paginator = Paginator(lancamento, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search',
        'search_value': search_value,
    }

    return render(
        request,
        'app/listall.html',
        context
    )


# create your view here
def add_lancamento(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        data_lancamento = request.POST.get('data_lancamento')
        data_pagamento = request.POST.get('data_pagamento')
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        autor = request.POST.get('autor')
        nota = request.POST.get('nota')
        genero = request.POST.get('genero')

        lancamento = Lancamento(
            descricao=descricao,
            data_lancamento=data_lancamento,
            data_pagamento=data_pagamento,
            valor=valor,
            categoria=categoria,
            autor=autor,
            nota=nota,
            genero=genero,
        )
        lancamento.save()

        return redirect('app:listall')
    return render(request, 'app/listall.html')


def edit_lancamento(request):
    lancamento = Lancamento.objects.all()

    context = {
        'lancamento': lancamento,
    }
    return render(request, 'app/listall.html', context)


def update_lancamento(request, id):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        data_lancamento = request.POST.get('data_lancamento')
        data_pagamento = request.POST.get('data_pagamento')
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        autor = request.POST.get('autor')
        nota = request.POST.get('nota')
        genero = request.POST.get('genero')

        lancamento = Lancamento(
            id=id,
            descricao=descricao,
            data_lancamento=data_lancamento,
            data_pagamento=data_pagamento,
            valor=valor,
            categoria=categoria,
            autor=autor,
            nota=nota,
            genero=genero,
        )
        lancamento.save()

        return redirect('app:listall')

    return render(request, 'app/listall.html')


def delete_lancamento(request, id):
    Lancamento.objects.filter(id=id).delete()
    return redirect('app:listall')
