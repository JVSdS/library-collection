from database.init_db import create_tables
from database.categorias_repository import (
    adicionar_categoria,
    listar_categorias,
    categoria_existe,
    popular_categorias_padrao,
    deletar_categoria,
    categoria_tem_itens
)
from database.itens_repository import (
    adicionar_item,
    listar_itens,
    atualizar_item,
    deletar_item,
    item_existe
)
from models.item import Item
from models.category import Categoria


create_tables()
popular_categorias_padrao()


def exibir_menu():
    print("\n─୨ৎ─ Biblioteca - Sistema de Acervo ─୨ৎ─")
    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Atualizar item")
    print("4 - Deletar item")
    print("5 - Adicionar categoria")
    print("6 - Listar categorias")
    print("7 - Deletar categoria")
    print("0 - Sair")

def cadastrar_item():
    try:
        print("\nCADASTRAR NOVO ITEM")

        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        ano = int(input("Ano: "))
        tipo = input("Tipo: ").strip()

        print("\nCategorias disponíveis:")
        categorias = listar_categorias()
        for i in categorias:
            print(f" {i.id} - {i.nome}")

        categoria_id = int(input("\nID da Categoria: "))

        if not categoria_existe(categoria_id):
            print("Erro: Categoria não encontrada!")
            return
        
        item = Item(titulo, autor, ano, categoria_id, tipo)

        adicionar_item(item)
        print("Item adicionado com sucesso!")

    except ValueError as e:
        print(f"Erro de validação: {e}")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")

def listar_itens_menu():
    itens = listar_itens()

    if not itens:
        print("\nNenhum item cadastrado.")
        return
    
    print("\n─୨ৎ─ Lista de Itens ─୨ৎ─\n")

    for item_obj, categoria_nome in itens:
        print(f"ID: {item_obj.id}")
        print(f"Título: {item_obj.titulo}")
        print(f"Autor: {item_obj.autor}")
        print(f"Ano: {item_obj.ano}")
        print(f"Tipo: {item_obj.tipo}")
        print(f"Categoria: {categoria_nome if categoria_nome else 'Sem categoria'}")
        print("-" * 30)

def atualizar_item_menu():
    try:

        print("\n─୨ৎ─ Atualizar item ─୨ৎ─")

        item_id = int(input("ID do item a atualizar: "))

        if not item_existe(item_id):
            print("Erro: Item não encontrado!")
            return

        titulo = input("Novo título: ").strip()
        autor = input("Novo autor: ").strip()
        ano = int(input("Novo ano: "))
        tipo = input("Novo tipo: ").strip()

        print("\nCategorias disponíveis: ")
        categorias = listar_categorias()
        for i in categorias:
            print(f" {i.id} - {i.nome}")

        categoria_id = int(input("\nNovo ID da Categoria: "))

        if not categoria_existe(categoria_id):
            print("Erro: Categoria não encontrada!")
            return

        item = Item(titulo, autor, ano, categoria_id, tipo, id=item_id)
        atualizar_item(item)
        print("Item atualizado com sucesso!")

    except ValueError as e:
        print(f"Erro de validação: {e}")
    except Exception as e:
        print(f"Erro ao atualizar: {e}")

def deletar_item_menu():
    try:

        listar_itens_menu()

        print("\n─୨ৎ─ Deletar item ─୨ৎ─")

        item_id = int(input("ID do item a deletar: "))

        if not item_existe(item_id):
            print("Erro: Item não encontrado")
            return
        
        confirma = input("Tem certeza? (S/N): ").strip().upper()

        if confirma == 'S':
            deletar_item(item_id)
            print("Item deletado com sucesso!")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("Erro: ID deve ser número.")
    except Exception as e:
        print(f"Erro ao deletar: {e}")

def cadastrar_categoria():
    try:
        print("\n─୨ৎ─ Cadastrar nova categoria ─୨ৎ─")

        nome = input("Nome da categoria: ").strip()

        categoria = Categoria(nome)

        adicionar_categoria(categoria)
        print("Categoria adicionada com sucesso!")

    except ValueError as e:
        print(f"Erro de validação: {e}")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")

def listar_categorias_menu():
    categorias = listar_categorias()

    if not categorias:
        print("\nNenhuma categoria cadastrada")
        return
    
    print("─୨ৎ─ Categorias ─୨ৎ─")

    for i in categorias:
        print(f"{i.id} - {i.nome}")

def deletar_categoria_menu():
    try:
        print("\n─୨ৎ─ Deletar categoria ─୨ৎ─")

        listar_categorias_menu()

        categoria_id = int(input("\nID da categoria a deletar: "))

        if not categoria_existe(categoria_id):
            print("Erro: Categoria não encontrada!")
            return
        
        if categoria_tem_itens(categoria_id):
            print("Erro: Não é possível excluir. Existem itens vinculados a essa categoria.")
            return
        
        confirma = input("Tem certeza? (S/N): ").strip().upper()

        if confirma == "S":
            deletar_categoria(categoria_id)
            print("Categoria deletada com sucesso!")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("Erro: ID deve ser número")
    except Exception as e:
        print(f"Erro ao deletar categoria: {e}")

def main():
    print("\nBem-vindo ao Sistema de Acervo")

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
        elif opcao == "5":
            cadastrar_categoria()
        elif opcao == "6":
            listar_categorias_menu()
        elif opcao == "7":
            deletar_categoria_menu()
        elif opcao == "0":
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida. Tente outro número.")

if __name__ == "__main__":
    main()