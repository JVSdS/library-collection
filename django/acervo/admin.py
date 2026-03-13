from django.contrib import admin
from .models import Categoria, Item, SugestaoItem, ListaUsuario, Favorito

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'formatado_ano', 'tipo', 'exibir_categorias']
    list_filter = ['tipo', 'ano']
    search_fields = ['titulo', 'autor']
    date_hierarchy = 'criado_em'

    @admin.display(description='Ano')
    def formatado_ano(self, obj):
        return obj.formatar_ano()
    
    @admin.display(description='Categorias')
    def exibir_categorias(self, obj):
        return ", ".join([c.nome for c in obj.categoria.all()])
    
admin.site.register(SugestaoItem)
admin.site.register(ListaUsuario)

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'item', 'data_adicionado')
    list_filter = ('usuario', 'item')