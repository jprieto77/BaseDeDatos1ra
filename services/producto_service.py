import mysql.connector

def get_all_products():
    conn = mysql.connector.connect(
        host='localhost',
    port=3306,
    user='root',  # Asegúrate de incluir el usuario
    password="12345",
    database="gestion_compras"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Productos")
    products = cursor.fetchall()
    conn.close()
    return products

def create_product(product_data):
    conn = mysql.connector.connect(
           host='localhost',  
    port=3306, password="12345", database="gestion_compras"
    )
    cursor = conn.cursor()
    query = """
        INSERT INTO Productos (nombre, precio, stock)
        VALUES (%s, %s, %s,)
    """
    cursor.execute(query, (
        product_data['nombre'],
        product_data['precio'],
        product_data['stock']
       
    ))
    conn.commit()
    conn.close()
    return {"message": "Producto creado con éxito"}
