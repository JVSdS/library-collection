from database.connection import get_connection
from models.item import Item

def adicionar_item(item):

    item.validar()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO itens (titulo, autor, ano, categoria_id, tipo)
        VALUES (?, ?, ?, ?, ?)
    """, (item.titulo, item.autor, item.ano, item.categoria_id, item.tipo))

    conn.commit()
    conn.close()

def listar_itens():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT itens.id,
            itens.titulo,
            itens.autor,
            itens.ano,
            itens.tipo,
            categorias.nome,
            itens.categoria_id
        FROM itens
        LEFT JOIN categorias ON itens.categoria_id = categorias.id
        """)

    resultados = cursor.fetchall()
    conn.close()

    itens = []
    for row in resultados:
        item = Item(
            id=row[0],
            titulo=row[1],
            autor=row[2],
            ano=row[3],
            tipo=row[4],
            categoria_id=row[6]
        )
        itens.append((item, row[5]))

    return itens

def atualizar_item(item):

    item.validar()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE itens
        SET titulo = ?, autor = ?, ano = ?, categoria_id = ?, tipo = ?
        WHERE id = ?
    """, (item.titulo, item.autor, item.ano, item.categoria_id, item.tipo, item.id))

    conn.commit()
    conn.close()

def deletar_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM itens WHERE id = ?", (item_id,))

    conn.commit()
    conn.close()

def item_existe(item_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM itens WHERE id = ?", (item_id,))
    count = cursor.fetchone()[0]

    conn.close()
    return count > 0