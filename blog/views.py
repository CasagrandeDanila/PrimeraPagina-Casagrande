from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AutorForm, PostForm, ComentarioForm, BuscarPostForm
from .models import Post

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorForm()
    return render(request, 'blog/autor.html', {'form': form})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {'form': form})

def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ComentarioForm()
    return render(request, 'blog/comentario.html', {'form': form})

def buscar_post(request):
    resultados = None
    if request.method == "POST":
        form = BuscarPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarPostForm()
    return render(request, 'blog/buscar_post.html', {'form': form, 'resultados': resultados})

def inicio(request):
    return render(request, 'blog/inicio.html')
