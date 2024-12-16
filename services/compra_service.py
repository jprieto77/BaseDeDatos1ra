import mysql.connector

def create_purchase(purchase_data):
    conn = mysql.connector.connect(
          host='localhost',
    port=3306,
    user='root',  # Asegúrate de incluir el usuario
    password="12345",
    database="gestion_compras"
    )
    cursor = conn.cursor()
    
    # Registrar la compra
    cursor.execute("""
        INSERT INTO Compras (cliente_id, producto_id, cantidad)
        VALUES (%s, %s, %s)
    """, (
        purchase_data['cliente_id'],
        purchase_data['producto_id'],
        purchase_data['cantidad']
    ))

    # Actualizar stock del producto
    cursor.execute("""
        UPDATE Productos SET stock = stock - %s WHERE id = %s
    """, (
        purchase_data['cantidad'],
        purchase_data['producto_id']
    ))

    conn.commit()
    conn.close()
    return {"message": "Compra realizada y stock actualizado"}
