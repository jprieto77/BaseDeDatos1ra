# app/models/devolucion.py

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
    port=3306,
    user='root',  
    password="12345",
    database="gestion_compras"
    )

def crear_devolucion(cliente_id, producto_id, motivo):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO devoluciones (cliente_id, producto_id, motivo)
        VALUES (%s, %s, %s)
    """, (cliente_id, producto_id, motivo))
    
    conn.commit()
    cursor.close()
    conn.close()

def obtener_devoluciones():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devoluciones")
    devoluciones = cursor.fetchall()
    cursor.close()
    conn.close()
    return devoluciones
