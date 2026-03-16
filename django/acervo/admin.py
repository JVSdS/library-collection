from django.contrib import admin
from django import forms
from .models import Categoria, Item, ListaUsuario, Favorito, TipoItem

class ItemAdminForm(forms.ModelForm):
    tipo_selecao = forms.ModelChoiceField(
        queryset=TipoItem.objects.all(),
        required=False,
        label="Tipo de Item (Selecione um cadastrado)",
    )

    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.tipo:
            tipo_obj = TipoItem.objects.filter(nome=self.instance.tipo).first()
            if tipo_obj:
                self.fields['tipo_selecao'].initial = tipo_obj

    def save(self, commit=True):
        tipo_obj = self.cleaned_data.get('tipo_selecao')
        if tipo_obj:
            self.instance.tipo = tipo_obj.nome
        return super().save(commit=commit)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(TipoItem)
class TipoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ['id', 'titulo', 'autor', 'tipo', 'formatado_ano', 'exibir_categorias']
    list_filter = ['tipo', 'categoria', 'ano']
    search_fields = ['titulo', 'autor']
    date_hierarchy = 'criado_em'

    @admin.display(description='Ano')
    def formatado_ano(self, obj):
        return obj.formatar_ano()
    
    @admin.display(description='Categorias')
    def exibir_categorias(self, obj):
        return ", ".join([c.nome for c in obj.categoria.all()])

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'item', 'data_adicionado')
    list_filter = ('usuario', 'item')

admin.site.register(ListaUsuario)