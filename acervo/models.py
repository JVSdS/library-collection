from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias"

    def clean(self):
        if not self.nome or not self.nome.strip():
            raise ValidationError("O nome da categoria não pode estar vazio")
        
    def __str__(self):
        return self.nome
    
class Item(models.Model):

    TIPO_CHOICES = [
        ('livro', 'Livro'),
        ('revista', 'Revista'),
        ('manuscrito', 'Manuscrito'),
        ('artigo', 'Artigo'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200, blank=True, default='Anônimo')
    ano = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='itens'
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Itens"
        ordering = ['-criado_em']

    def _ano_atual(self):
        return timezone.now().year

    def clean(self):
        if not self.titulo or not self.titulo.strip():
            raise ValidationError("O título não pode estar vazio")
    
        if not self.autor or not self.autor.strip():
            self.autor = "Anônimo"

        ano_atual = self._ano_atual()

        if self.ano < -3000:
            raise ValidationError("Ano muito antigo. Use anos após 3000 a.C.")
    
        if self.ano > ano_atual + 1:
            raise ValidationError(
                f"Ano não pode ser maior que {ano_atual + 1}. Cadastre apenas obras publicadas ou com lançamento confirmado"
            )
    
        if self.ano == 0:
            raise ValidationError("Ano 0 não existe. Use -1 (1 a.C.) ou 1 (1 d.C.)")
        
    def formatar_ano(self):
        if self.ano < 0:
            return f"{abs(self.ano)} a.C."
        return str(self.ano)

    def eh_pre_lancamento(self):
        return self.ano > self._ano_atual()


    def eh_classico(self):
        ano_atual = self._ano_atual()
        return self.ano <= ano_atual and (ano_atual - self.ano) > 50

    def eh_anonimo(self):
        return self.autor == "Anônimo"

    def __str__(self):
        ano_str = self.formatar_ano()
        badges = []

        if self.eh_pre_lancamento():
            badges.append("🚀")
        elif self.eh_classico():
            badges.append("📚")

        if self.eh_anonimo():
            badges.append("👤")

        badges_str = f" {' '.join(badges)}" if badges else "" 
        return f"{self.titulo} - {self.autor} ({ano_str}{badges_str})"