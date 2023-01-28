from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormAvaliacaoDiaria
from .models import AvaliacaoDiaria
from django.contrib import messages
from django.contrib.messages import constants


def home(request):
    avaliacoes = AvaliacaoDiaria.objects.all()

    return render(request, 'index.html', {'avaliacoes':avaliacoes})


def cadastro_avaliacao(request):
    if request.method == "POST":
        form = FormAvaliacaoDiaria(data=request.POST)
        try:
            if form.is_valid():
                form.save()
            messages.add_message(request, constants.SUCCESS,'Avaliacão inserida com sucesso!!!')
            return redirect('/')
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Dados inválidos, tente novamente!')
            return redirect('/')
    else:
        form = FormAvaliacaoDiaria()
        return render(request, 'form-avaliacao.html', {'form':form})


def deletar_avaliacao(request, id):
    try:
        avaliacao = AvaliacaoDiaria.objects.get(id=id)
        avaliacao.delete()
        messages.add_message(request, constants.SUCCESS, 'Avaliacao deletado com sucesso!')
        return redirect('/')
    except Exception as e:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar avaliacao!')
        return redirect('/')


def editar_avaliacao(request, id ):
    avalicao = AvaliacaoDiaria.objects.get(id=id)

    form = FormAvaliacaoDiaria(data=request.POST or None, instance=avalicao)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, constants.SUCCESS, f'Avaliacão alterada com sucesso!')
                return redirect('/')
        except Exception as e:
            pass
    elif request.method == 'GET':
        return render(request, 'form-avaliacao.html', {'form':form})
