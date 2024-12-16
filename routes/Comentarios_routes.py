from flask import Blueprint, request, jsonify
from models.comentarios import ComentariosManager

comentarios_bp = Blueprint('comentarios', __name__)
comentarios_manager = ComentariosManager()

# Agregar un nuevo comentario
@comentarios_bp.route('/productos/<int:producto_id>/comentarios', methods=['POST'])
def agregar_comentarios_endpoint(producto_id):
    try:
        data = request.get_json()
        usuario = data['usuario']
        comentario = data['comentario']
        calificacion = data['calificacion']

        comentarios_manager.agregar_comentario(
            producto_id=producto_id,
            usuario=usuario,
            comentario=comentario,
            calificacion=calificacion
        )
        return jsonify({"message": "Comentario agregado con éxito"}), 201
    except KeyError as e:
        return jsonify({"error": f"Falta el campo: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener todos los comentarios de un producto
@comentarios_bp.route('/productos/<int:producto_id>/comentarios', methods=['GET'])
def obtener_comentarios_endpoint(producto_id):
    try:
        comentarios = comentarios_manager.obtener_comentarios(producto_id)
        return jsonify(comentarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener la calificación promedio de un producto
@comentarios_bp.route('/productos/<int:producto_id>/calificacion', methods=['GET'])
def obtener_calificacion_endpoint(producto_id):
    try:
        calificacion = comentarios_manager.obtener_calificacion_promedio(producto_id)
        return jsonify(calificacion), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
