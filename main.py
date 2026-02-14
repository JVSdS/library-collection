from database.init_db import create_tables
from models.category import criar_categoria, listar_categorias
from database.itens_repository import (
    adicionar_item,
    listar_itens,
    atualizar_item,
    deletar_item
)

create_tables()


def exibir_menu():
    print("\n─୨ৎ─ Biblioteca ─୨ৎ─")
    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Atualizar item")
    print("4 - Deletar item")
    print("0 - Sair")

def cadastrar_item():
    try:
        titulo = input("Título: ").strip()
        if not titulo:
            print("O item precisa de um título, digite algo por favor e não deixe vazio.")
            return
        
        autor = input("Autor: ").strip()
        ano = int(input("Ano: "))
        categoria_id = int(input("Categoria ID: "))
        tipo = input("Tipo: ").strip()

        adicionar_item(titulo, autor, ano, categoria_id, tipo)
        print("Item adicionado com sucesso!")

    except ValueError:
        print("Erro: Ano e Categoria ID devem ser números.")

def listar_itens_menu():
    itens = listar_itens()
    if not itens:
        print("\nNenhum item cadastrado.")
        return
    
    print("\n─୨ৎ─ Lista de Itens ─୨ৎ─\n")
    for item in itens:
        id, titulo, autor, ano, tipo, categoria = item

        print(f"ID: {id}")
        print(f"Título: {titulo}")
        print(f"Autor: {autor}")
        print(f"Ano: {ano}")
        print(f"Tipo: {tipo}")
        print(f"Categoria: {categoria if categoria else 'Sem categoria'}")
        print("-" * 30)

def atualizar_item_menu():
    try:
        item_id = int(input("ID do item a atualizar: "))
        titulo = input("Novo título: ")
        autor = input("Novo autor: ")
        ano = int(input("Novo ano: "))
        categoria_id = int(input("Nova categoria ID: "))
        tipo = input("Novo tipo: ")

        atualizar_item(item_id, titulo, autor, ano, categoria_id, tipo)
        print("Item atualizado com sucesso!")

    except ValueError:
        print("Erro: ID, Ano e Categoria devem ser números.")

def deletar_item_menu():
    try:
        item_id = int(input("ID do item a deletar: "))
        deletar_item(item_id)
        print("Item deletado com sucesso!")
    except ValueError:
        print("Erro: ID deve ser número.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_item()
        elif opcao == "2":
            listar_itens_menu()
        elif opcao == "3":
            atualizar_item_menu()
        elif opcao == "4":
            deletar_item_menu()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()