from django.contrib import admin
from .models import Categoria, Item, SugestaoItem, ListaUsuario, Favorito

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'formatado_ano', 'tipo', 'categoria']
    list_filter = ['tipo', 'categoria', 'ano']
    search_fields = ['titulo', 'autor']
    date_hierarchy = 'criado_em'

    @admin.display(description='Ano')
    def formatado_ano(self, obj):
        return obj.formatar_ano()
    
    admin.site.register(SugestaoItem)
    admin.site.register(ListaUsuario)

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'item', 'data_adicionado')
    list_filter = ('usuario', 'item')