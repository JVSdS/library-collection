from database.connection import get_connection

def adicionar_item(titulo, autor, ano, categoria_id, tipo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO itens (titulo, autor, ano, categoria_id, tipo)
        VALUES (?, ?, ?, ?, ?)
    """, (titulo, autor, ano, categoria_id, tipo))

    conn.commit()
    conn.close()

def listar_itens():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT itens.id, itens.titulo, itens.autor, itens.ano, itens.tipo, categorias.nome
        FROM itens
        LEFT JOIN categorias ON itens.categoria_id = categorias.id
    """)

    itens = cursor.fetchall()
    conn.close()
    return itens

def deletar_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM itens WHERE id = ?", (item_id,))

    conn.commit()
    conn.close()

def atualizar_item(item_id, titulo, autor, ano, categoria_id, tipo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE itens
        SET titulo = ?, autor = ?, ano = ?, categoria_id = ?, tipo = ?
        WHERE id = ?
    """, (titulo, autor, ano, categoria_id, tipo, item_id))

    conn.commit()
    conn.close()