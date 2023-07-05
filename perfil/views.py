from django.shortcuts import render, redirect
from .models import Conta
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.
def home(request):
    return render(request, 'home.html')


def gerenciar(request):
    return render(request, 'gerenciar.html')


def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')

    if len(apelido.strip()) == 0 or len(banco.strip()) == 0 or len(tipo.strip()) == 0 or len(valor.strip()) == 0: # noqa
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos!') # noqa
        return redirect('/perfil/gerenciar/')

    conta = Conta(
        apelido=apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso!') # noqa
    return redirect('/perfil/gerenciar/')
