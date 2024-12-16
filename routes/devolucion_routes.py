# app/routes/devolucion_routes.py

from flask import Blueprint, request, jsonify
from models.devolucion import crear_devolucion, obtener_devoluciones

devolucion_bp = Blueprint('devolucion', __name__)

# Crear una nueva devolución
@devolucion_bp.route('/devoluciones', methods=['POST'])
def agregar_devolucion():
    data = request.get_json()
    cliente_id = data['cliente_id']
    producto_id = data['producto_id']
    motivo = data['motivo']
    
    crear_devolucion(cliente_id, producto_id, motivo)
    return jsonify({"message": "Devolución registrada con éxito"}), 201

# Obtener todas las devoluciones
@devolucion_bp.route('/devoluciones', methods=['GET'])
def obtener_todas_las_devoluciones():
    devoluciones = obtener_devoluciones()
    return jsonify(devoluciones)
