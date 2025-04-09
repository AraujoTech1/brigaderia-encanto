import sqlite3
import os
from datetime import datetime

DB_PATH = "brigaderia.db"

def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                sabor TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                data TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

def adicionar_coluna_data():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("ALTER TABLE pedidos ADD COLUMN data TEXT")
        conn.commit()
    except sqlite3.OperationalError:
        pass  # A coluna já existe
    conn.close()

def adicionar_pedido(id_pedido, nome, sabor, quantidade, data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pedidos (id, nome, sabor, quantidade, data)
        VALUES (?, ?, ?, ?, ?)
    """, (id_pedido, nome, sabor, quantidade, data))
    conn.commit()
    conn.close()

# Rodar a função uma vez para corrigir a tabela
adicionar_coluna_data()
