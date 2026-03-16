from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

class SugestaoItem(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    aprovado = models.BooleanField(default=False)

class TipoItem(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias"

    def clean(self):
        if not self.nome or not self.nome.strip():
            raise ValidationError("O nome da categoria não pode estar vazio")
        
    imagem = models.ImageField(upload_to='categorias/', blank=True, null=True)
        
    def __str__(self):
        return self.nome
    
class Item(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200, blank=True, default='Anônimo')
    ano = models.IntegerField()
    categoria = models.ManyToManyField(Categoria, blank=True, related_name='itens')
    tipo = models.CharField(max_length=100, null=True, blank=True)
    imagem = models.ImageField(upload_to='itens/', null=True, blank=True) # Movi para cima das properties
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Itens"
        ordering = ['-criado_em']

    def clean(self):
        if not self.titulo or not self.titulo.strip():
            raise ValidationError("O título não pode estar vazio")
        
        if not self.autor or not self.autor.strip():
            self.autor = "Anônimo"

        ano_atual = timezone.now().year
        if self.ano < -3000:
            raise ValidationError("Ano muito antigo. Use anos após 3000 a.C.")
        if self.ano > ano_atual + 1:
            raise ValidationError(f"Ano não pode ser maior que {ano_atual + 1}.")
        if self.ano == 0:
            raise ValidationError("Ano 0 não existe.")

    def formatar_ano(self):
        if self.ano < 0:
            return f"{abs(self.ano)} a.C."
        return str(self.ano)

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url
        return '/static/imagens/placeholder_item.png'

    def __str__(self):
        ano_str = self.formatar_ano()
        return f"{self.titulo} - {self.autor} ({ano_str})"
    
class ListaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    nota_pessoal = models.TextField(blank=True, null=True)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        unique_together = ('usuario', 'item')

    def __str__(self):
        return f"{self.usuario.username} - {self.item.titulo}"
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfis', default='perfis/default.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'