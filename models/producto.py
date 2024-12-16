import mysql.connector

# Función para obtener la conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="12345",
        database="gestion_compras"
    )

# Función para crear un producto
def crear_producto(nombre, precio, stock):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO productos (nombre, precio, stock)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (nombre, precio, stock))
    conn.commit()
    cursor.close()
    conn.close()

# Función para obtener todos los productos
def obtener_productos():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Consulta para obtener todos los productos
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return productos