from django.shortcuts import render, redirect
from .models import Estoque
from .form import transacaoForm

def home(request):
    dicionario = {}
    dicionario['dic'] = Estoque.objects.all()

    busca = request.GET.get('search')
    if busca:
        dicionario['dic'] = Estoque.objects.filter(descricao__icontains = busca)

    return render(request, 'controle/home.html', dicionario)


def nova_transacao(request):
    dicionario = {}
    form = transacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    dicionario['form'] = form
    return render(request, 'controle/form.html', dicionario)


def update(request, pk):
    dicionario = {}
    update = Estoque.objects.get(pk=pk)
    form = transacaoForm(request.POST or None, instance=update)

    if form.is_valid():
        form.save()
        return redirect('home')

    dicionario['form'] = form
    dicionario['obj'] = update
    return render(request, 'controle/form.html', dicionario)


def delete(request, pk):
    delete = Estoque.objects.get(pk=pk)
    delete.delete()
    return redirect('home')

