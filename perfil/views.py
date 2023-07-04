from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def gerenciar(request):
    return render(request, 'gerenciar.html')
