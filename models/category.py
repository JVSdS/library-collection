class Categoria:
    def __init__(self, nome, id=None):
        self.id = id
        self.nome = nome

    def validar_nome(self):
        if not self.nome or not self.nome.strip():
            raise ValueError("O nome da categoria não pode estar vazio")
        return True
    
    def __str__(self):
        return self.nome