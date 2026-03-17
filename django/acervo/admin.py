from django.contrib import admin
from .models import Categoria, Item, Favorito, TipoItem

admin.site.site_header = "Library Collection - Admin"
admin.site.site_title = "Library Collection"
admin.site.index_title = "Gerenciamento de Acervo"

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(TipoItem)
class TipoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'tipo', 'formatado_ano', 'exibir_categorias']
    list_filter = ['tipo', 'categoria', 'ano']
    search_fields = ['titulo', 'autor']
    
    fieldsets = (
        ("Informações Básicas", {
            'fields': ('titulo', 'autor', 'ano', 'tipo')
        }),
        ("Mídia e Categorias", {
            'fields': ('imagem', 'categoria')
        }),
    )

    @admin.display(description='Ano')
    def formatado_ano(self, obj):
        return obj.formatar_ano()
    
    @admin.display(description='Categorias')
    def exibir_categorias(self, obj):
        return ", ".join([c.nome for c in obj.categoria.all()])
    
    class Media:
        css = {
            'all': ('css/admin.css',)
        }

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'item', 'nota_pessoal', 'data_adicionado')
    list_filter = ('usuario',)