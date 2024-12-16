import mysql.connector

# Obtener cliente por ID
def get_client_by_id(client_id):
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="12345",
        database="gestion_compras"
    )
    cursor = conn.cursor(dictionary=True)
    
    # Extraer latitud y longitud junto con otros datos
    cursor.execute("""
        SELECT id, nombre, correo, telefono, Direccion,
               ST_X(ubicacion) AS latitud, ST_Y(ubicacion) AS longitud
        FROM clientes
        WHERE id = %s
    """, (client_id,))
    
    client = cursor.fetchone()
    cursor.close()
    conn.close()
    return client

# Crear un cliente
def create_client(client_data):
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="12345",
        database="gestion_compras"
    )
    cursor = conn.cursor()
    
    # Insertar datos, incluyendo la contraseña
    query = """
        INSERT INTO clientes (nombre, correo, telefono, Direccion, ubicacion, password)
        VALUES (%s, %s, %s, %s, ST_GeomFromText(%s), %s)
    """
    cursor.execute(query, (
        client_data['nombre'],
        client_data['correo'],
        client_data['telefono'],
        client_data['Direccion'],
        f"POINT({client_data['latitud']} {client_data['longitud']})",
        client_data['password']  # Incluimos la contraseña
    ))
    
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Cliente creado con éxito"}


# Actualizar un cliente
def update_client(client_id, client_data):
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="12345",
        database="gestion_compras"
    )
    cursor = conn.cursor()
    
    # Actualizar datos, incluyendo la contraseña si se envía
    query = """
        UPDATE clientes
        SET nombre = %s, correo = %s, telefono = %s, Direccion = %s, 
            ubicacion = ST_GeomFromText(%s)
    """
    
    # Si se proporciona una nueva contraseña, la actualizamos
    if 'password' in client_data:
        query += ", password = %s"
        cursor.execute(query + " WHERE id = %s", (
            client_data['nombre'],
            client_data['correo'],
            client_data['telefono'],
            client_data['Direccion'],
            f"POINT({client_data['latitud']} {client_data['longitud']})",
            client_data['password'],  # Incluimos la contraseña
            client_id
        ))
    else:
        cursor.execute(query + " WHERE id = %s", (
            client_data['nombre'],
            client_data['correo'],
            client_data['telefono'],
            client_data['Direccion'],
            f"POINT({client_data['latitud']} {client_data['longitud']})",
            client_id
        ))

    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Cliente actualizado con éxito"}


# Eliminar un cliente
def delete_client(client_id):
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="12345",
        database="gestion_compras"
    )
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM clientes WHERE id = %s", (client_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Cliente eliminado con éxito"}

# Obtener todos los clientes
def get_all_clients():
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="12345",
        database="gestion_compras"
    )
    cursor = conn.cursor(dictionary=True)
    
    # Extraer latitud y longitud junto con otros datos
    query = """
        SELECT id, nombre, correo, telefono, Direccion,
               ST_X(ubicacion) AS latitud, ST_Y(ubicacion) AS longitud
        FROM clientes
    """
    cursor.execute(query)
    clients = cursor.fetchall()
    cursor.close()
    conn.close()
    return clients
