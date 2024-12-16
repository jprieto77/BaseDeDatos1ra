import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="12345",
        database="gestion_compras"
    )

def crear_sucursal(nombre, latitud, longitud):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Usamos ST_GeomFromText para almacenar la ubicación como GEOMETRY
    cursor.execute("""
        INSERT INTO sucursales (nombre, ubicacion)
        VALUES (%s, ST_GeomFromText(%s))
    """, (nombre, f"POINT({latitud} {longitud})"))
    
    conn.commit()
    cursor.close()
    conn.close()

def obtener_sucursales():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Consultamos las sucursales y las convertimos a un formato comprensible
    cursor.execute("SELECT id, nombre, ST_X(ubicacion) AS latitud, ST_Y(ubicacion) AS longitud FROM sucursales")
    sucursales = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return sucursales
