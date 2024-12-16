import mysql.connector

# Configuración de conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',  # Cambiar si es necesario
        password='12345',  # Cambiar si es necesario
        database='gestion_compras'
    )

# Crear un nuevo cliente
def crear_cliente(nombre, correo, telefono, Direccion, latitud, longitud, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insertar datos en la tabla usando ST_GeomFromText, incluyendo la contraseña
    cursor.execute("""
        INSERT INTO clientes (nombre, correo, telefono, Direccion, ubicacion, password)
        VALUES (%s, %s, %s, %s, ST_GeomFromText(%s), %s)
    """, (nombre, correo, telefono, Direccion, f"POINT({latitud} {longitud})", password))
    
    conn.commit()
    cursor.close()
    conn.close()


# Obtener todos los clientes
def obtener_clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Consultar datos incluyendo latitud y longitud extraídos de la columna `ubicacion`
    cursor.execute("""
        SELECT id, nombre, correo, telefono, Direccion, 
               ST_X(ubicacion) AS latitud, ST_Y(ubicacion) AS longitud
        FROM clientes
    """)
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes

# Obtener un cliente por ID
def obtener_cliente_por_id(cliente_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("""
        SELECT id, nombre, correo, telefono, Direccion, 
               ST_X(ubicacion) AS latitud, ST_Y(ubicacion) AS longitud
        FROM clientes
        WHERE id = %s
    """, (cliente_id,))
    
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()
    return cliente

# Actualizar información de un cliente
def actualizar_cliente(cliente_id, nombre, correo, telefono, Direccion, latitud, longitud, password=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Actualizar datos, incluyendo la contraseña si se proporciona
    query = """
        UPDATE clientes
        SET nombre = %s, correo = %s, telefono = %s, Direccion = %s, 
            ubicacion = ST_GeomFromText(%s)
    """
    
    # Si se proporciona una nueva contraseña, la actualizamos
    if password:
        query += ", password = %s"
        cursor.execute(query + " WHERE id = %s", (
            nombre, correo, telefono, Direccion, f"POINT({latitud} {longitud})", password, cliente_id
        ))
    else:
        cursor.execute(query + " WHERE id = %s", (
            nombre, correo, telefono, Direccion, f"POINT({latitud} {longitud})", cliente_id
        ))

    conn.commit()
    cursor.close()
    conn.close()


# Eliminar un cliente
def eliminar_cliente(cliente_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
    
    conn.commit()
    cursor.close()
    conn.close()
