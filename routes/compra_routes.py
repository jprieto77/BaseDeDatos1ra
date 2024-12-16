# app/routes/compra_routes.py

from flask import Blueprint, request, jsonify
from models.compra import crear_compra, obtener_compras

compra_bp = Blueprint('compra_bp', __name__)

# Crear una nueva compra
@compra_bp.route('/compras', methods=['POST'])
def agregar_compra():
    data = request.get_json()
    cliente_id = data['cliente_id']
    producto_id = data['producto_id']
    cantidad = data['cantidad']

    try:
        crear_compra(cliente_id, producto_id, cantidad)
        return jsonify({"message": "Compra registrada con éxito"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500