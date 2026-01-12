from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={'name':'Luiz Otavio'})
def sobre(request):
    return render(request, 'temp/git push origin maintemp.html')
def contato(request):
    return render(request, 'recipes/contato.html')