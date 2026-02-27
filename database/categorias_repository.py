from database.connection import get_connection
from models.category import Categoria

def adicionar_categoria(categoria):
    categoria.validar_nome()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (categoria.nome,))

    conn.commit()
    conn.close()

def listar_categorias():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM categorias")
    resultados = cursor.fetchall()

    conn.close()

    categorias = []
    for row in resultados:
        i = Categoria(id=row[0], nome=row[1])
        categorias.append(i)

    return categorias

def categoria_existe(categoria_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM categorias WHERE id = ?", (categoria_id,))
    count = cursor.fetchone()[0]

    conn.close()
    return count > 0

def popular_categorias_padrao():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM categorias")
    count = cursor.fetchone()[0]

    if count == 0:
        categorias_padrao = [
            "Ficção",
            "Não-Ficção",
            "Romance",
            "Técnico",
            "Infantil",
            "Biografia"
        ]

        for nome in categorias_padrao:
            cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))

        conn.commit()
        print("Categoria(s) padrão criada(s) com sucesso!")

        conn.close()

def deletar_categoria(id_categoria):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM categorias WHERE id = ?", (id_categoria,))
    conn.commit()
    conn.close()

def categoria_tem_itens(categoria_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM itens WHERE categoria_id = ?",
        (categoria_id,)
    )

    count = cursor.fetchone()[0]
    conn.close()
    return count > 0