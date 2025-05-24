from django.shortcuts import render, redirect
from .models import Produto, UserProfile
from django.conf import settings
from .forms import ProdutoForm, ProfileForm
import os

def home(request):
    return render(request, 'app1/home.html')

def produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'app1/produtos.html', {'produtos': produtos})

def contatos(request):
    return render(request, 'app1/contatos.html')


def list_profile_pics(request):
    """
    Lista todas as imagens de perfil usando a OS Library.
    """
    pics_path = os.path.join(settings.MEDIA_ROOT, 'profile_pics')
    pictures = [f for f in os.listdir(pics_path) if f.endswith(('.jpg', '.png'))]
    return render (request, 'list_pics.html', {'pictures': pictures})

def add_produto(request):
    if request.method == 'POST':
        form = ProdutoForm (request.POST, request.FILES)  # Note o request.FILES!
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'app1/add_produto.html', {'form': form})

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'app1/upload_profile.html', {'form': form})