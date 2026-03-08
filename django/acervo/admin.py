from django.contrib import admin
from .models import Categoria, Item

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