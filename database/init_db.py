from database.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabela de categorias
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    # Tabela de livros
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT,
            ano INTEGER,
            categoria_id INTEGER,
            tipo TEXT NOT NULL,
            criado_em TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (categoria_id) REFERENCES categorias (id)
        )
    """)

    conn.commit()
    conn.close()