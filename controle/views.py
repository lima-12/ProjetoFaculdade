from django.shortcuts import render
from .models import transacao


def home(request):
    dicionario = {}
    dicionario['dic'] = transacao.objects.all()
    return render(request, 'controle/home.html', dicionario)
