from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from .models import Item, Categoria

def item_list(request):
    itens = Item.objects.all()
    return render(request, 'acervo/item_list.html', {'itens': itens})

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
            item.autor = request.POST.get('autor') or ('Anônimo')

            ano = request.POST.get('ano')
            if not ano:
                raise ValidationError("Ano é obrigatório")
            item.ano = int(ano)

            item.tipo = request.POST.get('tipo')
            categoria_id = request.POST.get('categoria')
            item.categoria_id = categoria_id if categoria_id else None

            item.full_clean()
            item.save()

            messages.success(request, f'Item "{item.titulo}" atualizado!')
            return redirect('item_list')
        
        except ValidationError as e:
            messages.error(request, f"Erro: {e.messages}")

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

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'acervo/categoria_list.html', {'categorias': categorias})