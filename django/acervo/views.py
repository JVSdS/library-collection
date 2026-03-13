from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Categoria, ListaUsuario, Favorito, Perfil
from django.core.exceptions import ValidationError
from django.contrib import messages

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
            return render(request, "registro.html")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Conta criada! Faça o login.")

        return redirect("login")
    
    return render(request, "registration/registro.html")

def adicionar_lista(request, item_id):
    item = Item.objects.get(id=item_id)

    ListaUsuario.objects.create(
        usuario=request.user,
        item=item
    )

    return redirect("item_list")

def item_create(request):
    if request.method == 'POST':
        try:
            titulo = request.POST.get('titulo')
            autor = request.POST.get('autor') or ('Anônimo')
            ano = request.POST.get('ano')
            tipo = request.POST.get('tipo')
            categoria_id = request.POST.get('categoria')

            if not ano:
                raise ValidationError("Ano é obrigatório")
            
            ano = int(ano)

            item = Item(
                titulo=titulo,
                autor=autor,
                ano=ano,
                tipo=tipo,
                categoria_id=categoria_id if categoria_id else None
            )
            item.full_clean()
            item.save()

            messages.success(request, f'Item "{item.titulo}" adicionado com sucesso!')
            return redirect('item_list')
        
        except ValidationError as e:
            messages.error(request, f"Erro: {e.message}")
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar: {str(e)}")

    categorias = Categoria.objects.all()
    return render(request, 'acervo/item_form.html', {'categorias': categorias})

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
            item.tipo = request.POST.get('tipo')

            if 'imagem' in request.FILES:
                item.imagem = request.FILES['imagem']

            categoria_ids = request.POST.getlist('categorias')

            item.full_clean()
            item.save()

            if hasattr(item, 'categorias'):
                item.categorias.set(categoria_ids)
            elif hasattr(item, 'categoria'):
                item.categoria.set(categoria_ids)

            messages.success(request, f'Item "{item.titulo}" atualizado!')
            return redirect('item_list')
        
        except ValidationError as e:
            messages.error(request, f"Erro de validação: {e}")
        except Exception as e:
            messages.error(request, f"Erro inesperado: {e}")

    categorias = Categoria.objects.all()
    return render(request, 'acervo/item_form.html', {'item': item, 'categorias': categorias})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        titulo = item.titulo
        item.delete()
        messages.success(request, f'Item "{titulo}" deletado!')
        return redirect('item_list')
    
    return render(request, 'acervo/item_confirm_delete.html', {'item': item})

from django.shortcuts import render, get_object_or_404
from .models import Item, Categoria, Favorito

def item_list(request):
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        itens = Item.objects.filter(categoria__id=categoria_id)
        categoria_filtrada = get_object_or_404(Categoria, id=categoria_id)
    else:
        itens = Item.objects.all()
        categoria_filtrada = None

    favoritos_ids = []
    if request.user.is_authenticated:
        favoritos_ids = Favorito.objects.filter(usuario=request.user).values_list('item_id', flat=True)
    
    contexto = {
        'itens': itens,
        'categoria_filtrada': categoria_filtrada,
        'favoritos_ids': favoritos_ids,
    }

    return render(request, 'acervo/item_list.html', contexto)

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'acervo/categoria_list.html', {'categorias': categorias})

@login_required
def meus_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user)
    print(f"DEBUG: Usuário {request.user} tem {favoritos.count()} favoritos.")
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