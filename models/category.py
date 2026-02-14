from database.connection import get_connection

def criar_categoria(nome):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO categorias (nome) VALUES (?)",
        (nome,)
    )

    conn.commit()
    conn.close()

def listar_categorias():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()

    conn.close()
    return categorias