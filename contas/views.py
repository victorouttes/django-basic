from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime


def home(request):
    data = {
        'now': datetime.datetime.now(),
        'transacoes': ['t1', 't2', 't3']
    }
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {
        'transacoes': Transacao.objects.all()
    }
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form})


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form})
