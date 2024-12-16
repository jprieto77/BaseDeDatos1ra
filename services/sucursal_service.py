import mysql.connector

def get_all_branches():
    conn = mysql.connector.connect(
     host='localhost', port=3306, user="root", password="12345", database="gestion_compras"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sucursales")
    branches = cursor.fetchall()
    conn.close()
    return branches

def create_branch(branch_data):
    conn = mysql.connector.connect(
          host='localhost',  
    port=3306, 
        user='root',  
        password='12345', 
        database='gestion_compras'
    )
    cursor = conn.cursor()
    query = """
        INSERT INTO Sucursales (nombre, ubicacion)
        VALUES (%s, ST_GeomFromText(%s))
    """
    cursor.execute(query, (
        branch_data['nombre'],
        f"POINT({branch_data['latitud']} {branch_data['longitud']})"
    ))
    conn.commit()
    conn.close()
    return {"message": "Sucursal creada con éxito"}
