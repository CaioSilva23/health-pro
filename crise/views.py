from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from .models import AlertasCrise
from .forms import FormAlertasCrise, FormContato
from .models import Contato
from .sms import envia_sms

def crise(request):
    crises = AlertasCrise.objects.all()

    return render(request, 'crise.html', {'crises':crises})


def cadastro_crise(request):
    if request.method == "POST":
        form = FormAlertasCrise(data=request.POST)
        try:
            if form.is_valid():
                form.save()
            messages.add_message(request, constants.SUCCESS,'Crise registrada com sucesso!!!')
            return redirect('crise')
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Dados inválidos, tente novamente!')
            return redirect('crise')
    else:
        form = FormAlertasCrise()
        return render(request, 'form-crise.html', {'form':form})


def deletar_crise(request, id):
    try:
        avaliacao = get_object_or_404(AlertasCrise, id=id)
        avaliacao.delete()
        messages.add_message(request, constants.SUCCESS, 'Avaliacao deletado com sucesso!')
        return redirect('crise')
    except Exception as e:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar avaliacao!')
        return redirect('crise')


def editar_crise(request, id ):
    avalicao = get_object_or_404(AlertasCrise, id=id)

    form = FormAlertasCrise(data=request.POST or None, instance=avalicao)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, constants.SUCCESS, f'Crise alterada com sucesso!')
                return redirect('crise')
        except Exception as e:
            pass
    elif request.method == 'GET':
        return render(request, 'form-crise.html', {'form':form})


def envia_smss(request):
    contatos = Contato.objects.all()
    for contato in contatos:
        
        envia_sms(contato.celular)
    messages.add_message(request, constants.SUCCESS, 'Mensagem enviada')
    return redirect('crise')


def contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos.html', {'contatos': contatos})


def cadastro_contato(request):
    if request.method == "POST":
        form = FormContato(data=request.POST)
        try:
            if form.is_valid():
                form.save()
            messages.add_message(request, constants.SUCCESS,'Contato registrado com sucesso!!!')
            return redirect('contatos')
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Dados inválidos, tente novamente!')
            return redirect('contatos')
    else:
        form = FormContato()
        return render(request, 'form-contato.html', {'form':form})


def deletar_contato(request, id):
    try:
        contato = get_object_or_404(Contato, id=id)
        contato.delete()
        messages.add_message(request, constants.SUCCESS, 'Contato deletado com sucesso!')
        return redirect('contatos')
    except Exception as e:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar avaliacao!')
        return redirect('contatos')


def editar_contato(request, id ):
    avalicao = get_object_or_404(Contato, id=id)

    form = FormContato(data=request.POST or None, instance=avalicao)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, constants.SUCCESS, f'Contato alterado com sucesso!')
                return redirect('contatos')
        except Exception as e:
            pass
    elif request.method == 'GET':
        return render(request, 'form-contato.html', {'form':form})