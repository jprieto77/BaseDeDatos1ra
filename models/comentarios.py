import datetime
from pymongo import MongoClient

class ComentariosManager:
    def __init__(self):
        self.db = self.get_mongo_connection()

    def get_mongo_connection(self):
        client = MongoClient("mongodb+srv://JULIANSARAIVAN:IVANJULIANSARA@clusterbdfinal.4baix.mongodb.net/")
        db = client['TrabajofinalBD']
        return db

    def agregar_comentario(self, producto_id, usuario, comentario, calificacion):
        coleccion_comentarios = self.db['comentarios']

        # Insertar el comentario en la colección de comentarios
        coleccion_comentarios.insert_one({
            "producto_id": producto_id,
            "usuario": usuario,
            "comentario": comentario,
            "calificacion": calificacion,
            "fecha": datetime.datetime.now().isoformat()
        })

        # Calcular promedio y actualizar en la colección promedio_calificacion
        self.actualizar_productos_calificados(producto_id)

    def actualizar_promedio_calificacion(self, producto_id):
        coleccion_comentarios = self.db['comentarios']
        coleccion_ProductosCalificados = self.db['ProductosCalificados']

        # Calcular la nueva calificación promedio
        comentarios_producto = coleccion_comentarios.find({"producto_id": producto_id})
        calificaciones = [c["calificacion"] for c in comentarios_producto]
        calificacion_promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0

        # Actualizar o crear el promedio en la colección promedio_calificacion
        coleccion_ProductosCalificados.update_one(
            {"producto_id": producto_id},
            {"$set": {"calificacion_promedio": calificacion_promedio}},
            upsert=True
        )

    def obtener_comentarios(self, producto_id):
        coleccion_comentarios = self.db['comentarios']
        return list(coleccion_comentarios.find({"producto_id": producto_id}, {"_id": 0}))

    def obtener_calificacion_promedio(self, producto_id):
        coleccion_ProductosCalificados = self.db['promedio_calificacion']
        resultado = coleccion_ProductosCalificados.find_one({"producto_id": producto_id}, {"_id": 0})
        return resultado if resultado else {"producto_id": producto_id, "calificacion_promedio": 0}
