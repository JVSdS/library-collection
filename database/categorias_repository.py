from database.connection import get_connection

def criar_categoria(nome):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

def listar_categorias():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM categorias")
    categorias = cursor.fetchall()

    conn.close()
    return categorias

def deletar_categoria(id_categoria):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM categorias WHERE id = ?", (id_categoria,))
    conn.commit()
    conn.close()