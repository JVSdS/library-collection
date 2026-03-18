from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Categoria, Favorito, TipoItem
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db.models import Q
import random

def home(request):
    if request.user.is_authenticated:
        return redirect('item_list')
    return render(request, 'acervo/home.html')

def registrar(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Este nome de usuário já está em uso.")
            return render(request, "registration/registro.html")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Conta criada! Faça o login.")
        return redirect("login")
    
    return render(request, "registration/registro.html")

def item_create(request):
    if request.method == 'POST':
        try:
            titulo = request.POST.get('titulo')
            autor = request.POST.get('autor') or 'Anônimo'
            ano = request.POST.get('ano')
            tipo = request.POST.get('tipo')
            categoria_ids = request.POST.getlist('categorias')
            tipo_id = request.POST.get('tipo')

            if not ano:
                raise ValidationError("Ano é obrigatório")
            
            item = Item(
                titulo=titulo,
                autor=autor,
                ano=int(ano),
            )
            if tipo_id:
                item.tipo = TipoItem.objects.get(id=tipo_id)
            
            if 'imagem' in request.FILES:
                item.imagem = request.FILES['imagem']

            item.full_clean()
            item.save()

            if categoria_ids:
                item.categoria.set(categoria_ids)

            messages.success(request, f'Item "{item.titulo}" adicionado com sucesso!')
            return redirect('item_list')
        
        except ValidationError as e:
            messages.error(request, f"Erro: {e}")
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar: {str(e)}")

    contexto = {
        'categorias': Categoria.objects.all(),
        'tipos_disponiveis': TipoItem.objects.all(),
    }
    return render(request, 'acervo/item_form.html', contexto)

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        try:
            item.titulo = request.POST.get('titulo')
            item.autor = request.POST.get('autor') or 'Anônimo'
            
            ano = request.POST.get('ano')
            if not ano:
                raise ValidationError("Ano é obrigatório")
            item.ano = int(ano)

            tipo_id = request.POST.get('tipo')
            if tipo_id:
                item.tipo = get_object_or_404(TipoItem, id=tipo_id)
            else:
                item.tipo = None

            if 'imagem' in request.FILES:
                item.imagem = request.FILES['imagem']

            categoria_ids = request.POST.getlist('categorias')

            item.full_clean()
            item.save()

            item.categoria.set(categoria_ids)

            messages.success(request, f'Item "{item.titulo}" atualizado!')
            return redirect('item_list')
        
        except ValidationError as e:
            messages.error(request, f"Erro de validação: {e}")
        except Exception as e:
            messages.error(request, f"Erro inesperado: {e}")

    categorias = Categoria.objects.all()

    contexto = {
        'item': item,
        'categorias': Categoria.objects.all(),
        'tipos_disponiveis': TipoItem.objects.all(),
    }
    return render(request, 'acervo/item_form.html', contexto)

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        titulo = item.titulo
        item.delete()
        messages.success(request, f'Item "{titulo}" deletado!')
        return redirect('item_list')
    
    return render(request, 'acervo/item_confirm_delete.html', {'item': item})

def item_list(request):
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')
    
    itens = Item.objects.all().select_related('tipo').prefetch_related('categoria')

    lista_itens = list(itens)
    itens_aleatorios = random.sample(lista_itens, min(len(lista_itens), 2))

    if query:
        itens = itens.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query)
        )
    
    categoria_filtrada = None
    if categoria_id:
        itens = itens.filter(categoria__id=categoria_id)
        categoria_filtrada = get_object_or_404(Categoria, id=categoria_id)

    favoritos_ids = []
    if request.user.is_authenticated:
        favoritos_ids = Favorito.objects.filter(usuario=request.user).values_list('item_id', flat=True)
    
    contexto = {
        'itens': itens,
        'categoria_filtrada': categoria_filtrada,
        'favoritos_ids': favoritos_ids,
        'query': query,
        'itens_cabecalho': itens_aleatorios,
    }

    return render(request, 'acervo/item_list.html', contexto)

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'acervo/categoria_list.html', {'categorias': categorias})

@login_required
def meus_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, 'acervo/meus_favoritos.html', {'favoritos': favoritos})

@login_required
def adicionar_favorito(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    Favorito.objects.get_or_create(usuario=request.user, item=item)
    return redirect('perfil')

@login_required
def perfil_usuario(request):
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('item')
    total_favoritos = favoritos.count()

    from .models import Perfil
    perfil_usuario, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'foto_perfil' in request.FILES:
            perfil_usuario.foto = request.FILES['foto_perfil']
            perfil_usuario.save()
            messages.success(request, 'Sua foto de perfil foi atualizada!')
            return redirect('perfil')

    contexto = {
        'favoritos': favoritos,
        'total_favoritos': total_favoritos,
        'perfil': perfil_usuario,
    }
    return render(request, 'acervo/perfil.html', contexto)

@login_required
def remover_favorito(request, favorito_id):
    favorito = get_object_or_404(Favorito, id=favorito_id, usuario=request.user)
    favorito.delete()

    return redirect('perfil')

@login_required
def atualizar_nota(request, favorito_id):
    if request.method == 'POST':
        favorito = get_object_or_404(Favorito, id=favorito_id, usuario=request.user)
        nova_nota = request.POST.get('nota')
        favorito.nota_pessoal = nova_nota
        favorito.save()
        messages.success(request, 'Sua nota foi atualizada com sucesso!')
        
    return redirect('perfil')

def lista_categorias(request):
    categorias = Categoria.objects.all()
    contexto = {
        'categorias': categorias,
    }
    return render(request, 'acervo/categorias.html', contexto)