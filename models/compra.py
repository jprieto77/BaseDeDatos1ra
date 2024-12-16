# app/models/compra.py

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
           host='localhost',
    port=3306,
    user='root',  # Asegúrate de incluir el usuario
    password="12345",
    database="gestion_compras"
    )

def crear_compra(cliente_id, producto_id, cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO compras (cliente_id, producto_id, cantidad)
        VALUES (%s, %s, %s)
    """, (cliente_id, producto_id, cantidad))
    
    conn.commit()
    cursor.close()
    conn.close()

def obtener_compras():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compras")
    compras = cursor.fetchall()
    cursor.close()
    conn.close()
    return compras
