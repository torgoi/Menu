from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import DkangoForm
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    poko = Dkango.objects.all()
    context = {
        'poko': poko,
        'menu': menu,
        'title': 'kachok'
    }
    return render(request, 'index.html',context=context)

def general(request):
    poko = Dkango.objects.all()
    form = DkangoForm(request.POST or None)
    if request.method == 'POST':
        if 'save' in request.POST:
            if form.is_valid():
                form.save()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            fox = Dkango.objects.get(id=pk)
            fox.delete()
            return redirect('general')

    return render(request,'general.html',{'form':form,'poko':poko})

def addpage(request):
    return HttpResponse('Add page')
def contact(request):
    return HttpResponse('Contact')
def login(request):
    return HttpResponse('Login')


# Create your views here.
