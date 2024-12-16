import mysql.connector

def create_return(return_data):
    conn = mysql.connector.connect(
       host='localhost',
    port=3306,
    user='root',  # Asegúrate de incluir el usuario
    password="12345",
    database="gestion_compras"
    )
    cursor = conn.cursor()

    # Registrar la devolución
    cursor.execute("""
        INSERT INTO Devoluciones (cliente_id, producto_id, motivo)
        VALUES (%s, %s, %s)
    """, (
        return_data['cliente_id'],
        return_data['producto_id'],
        return_data['motivo']
    ))

    # Actualizar stock del producto
    cursor.execute("""
        UPDATE Productos SET stock = stock + %s WHERE id = %s
    """, (
        return_data['cantidad'],
        return_data['producto_id']
    ))

    conn.commit()
    conn.close()
    return {"message": "Devolución registrada y stock actualizado"}
