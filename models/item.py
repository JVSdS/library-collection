import datetime

class Item:
    def __init__(self, titulo, autor, ano, categoria_id, tipo, id=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria_id = categoria_id
        self.tipo = tipo

    def validar_titulo(self):
        if not self.titulo or not self.titulo.strip():
            raise ValueError("O título não pode estar vazio")
    
    def validar_autor(self):

        if not self.autor or not self.autor.strip():
            self.autor = "Anônimo"
            return True
        
        self.autor = self.autor.strip()
        
        if len(self.autor) > 200:
            raise ValueError("Nome do autor muito longo (máximo de 200 caracteres)")

        return True
        
    def validar_ano(self):
        ano_atual = datetime.datetime.now().year

        if self.ano < -3000:
            raise ValueError("Ano muito antigo, escolha após 3000 a.C.")
        
        if self.ano > ano_atual + 1:
            raise ValueError(f"O ano não pode ser maior que {ano_atual + 1}\n" 
                             "Cadastre apenas obras publicadas ou com lançamento confirmado para o próximo ano"
                             )
        
        if self.ano == 0:
            raise ValueError("Ano 0 não existe")
        
        return True
    
    def validar_tipo(self):
        if not self.tipo or not self.tipo.strip():
            raise ValueError("O tipo não pode estar vazio")
        
        self.tipo = self.tipo.strip().lower()

        sugestao = ['livro', 'revista', 'manuscrito', 'artigo', 'outro']

        if self.tipo not in sugestao:
            print(f"Tipo {self.tipo} aceito. Tipos mais comuns: {', '.join(sugestao[:3])}...")
        
        return True
    
    def validar(self):
        self.validar_titulo()
        self.validar_autor()
        self.validar_ano()
        self.validar_tipo()
        return True
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"