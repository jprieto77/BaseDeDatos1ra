from flask import Flask, render_template
from routes.cliente_routes import cliente_bp  # Importar el Blueprint
from flask import Flask, request, redirect, url_for, render_template, flash, Blueprint, jsonify
from flask import session  # Para manejar la sesión del usuario
import mysql.connector  
from routes.compra_routes import compra_bp
from routes.producto_routes import producto_bp


app = Flask(__name__)

# Registrar el Blueprint para clientes
app.register_blueprint(cliente_bp, url_prefix="/api")  # Prefijo opcional
app.register_blueprint(compra_bp)
app.register_blueprint(producto_bp, url_prefix='/api')

# Punto de entrada
if __name__ == "__main__":
    app.run(debug=True)

# Ruta principal
@app.route("/")
def home():
    return render_template("home.html")

# Ruta para la página de inicio cuando el usuario esta logeado
@app.route("/home2.html")
def home_page():
    return render_template("home2.html")


app.secret_key = 'mi_clave_secreta_super_segura_123456789'

# Conexión a la base de datos MySQL
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='gestion_compras'
    )

# Ruta para manejar el registro de clientes
@app.route('/api/clientes', methods=['POST'])
def register_client():
    try:
        data = request.get_json()  # Obtener los datos JSON del cuerpo de la solicitud
        nombre = data.get('nombre')
        correo = data.get('correo')
        password = data.get('password')
        telefono = data.get('telefono', '')
        direccion = data.get('Direccion', '')
        latitud = data.get('latitud')
        longitud = data.get('longitud')

        if not nombre or not correo or not password:
            return jsonify({'error': 'Faltan datos requeridos'}), 400

        # Crear la conexión a la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()

        # Crear el punto de ubicación (tipo GEOMETRY)
        cursor.execute("""
            INSERT INTO clientes (nombre, correo, telefono, Direccion, ubicacion, password) 
            VALUES (%s, %s, %s, %s, ST_GeomFromText('POINT(%s %s)'), %s)
        """, (nombre, correo, telefono, direccion, longitud, latitud, password))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Usuario registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Ruta para manejar el inicio de sesión
@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()  # Obtener el cuerpo de la solicitud en formato JSON
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Faltan datos'}), 400  # Si faltan datos, retornar 400

        # Conexión a la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()

        # Consulta a la base de datos para obtener el nombre y la contraseña
        cursor.execute("SELECT nombre, password FROM clientes WHERE correo = %s", (email,))
        result = cursor.fetchone()

        if result:
            stored_name, stored_password = result  # Obtenemos el nombre y la contraseña almacenada
            # Comparar la contraseña ingresada con la almacenada
            if password == stored_password:  # Comparación directa
                session['user'] = {'email': email, 'name': stored_name}  # Guardar el correo y el nombre en la sesión
                conn.close()
                return jsonify({'message': 'Login exitoso'}), 200  # Respuesta exitosa
            else:
                conn.close()
                return jsonify({'message': 'Contraseña incorrecta'}), 400
        else:
            conn.close()
            return jsonify({'message': 'Correo no registrado'}), 400

    except Exception as e:
        return jsonify({'message': str(e)}), 500  # Manejar errores inesperados


# Ruta para obtener los datos del usuario logueado
@app.route('/api/user', methods=['GET'])
def get_user():
    if 'user' in session:
        return jsonify({'user': session['user']}), 200
    else:
        return jsonify({'message': 'Usuario no autenticado'}), 401


# Ruta para la página de login
@app.route("/Login.html")
def login_page():
    return render_template("Login.html")

@app.route("/Categorias.html")
def categorias():
    return render_template("Categorias.html")

# Ruta para la página de productos
@app.route("/Productos.html")
def products():
    return render_template("Productos.html")

# Ruta para la página de registrar
@app.route("/Register.html")
def register():
    return render_template("Register.html")

# Ruta para la página de sucursales cercanas
@app.route("/ubicacion.html")
def ubicacion():
    return render_template("ubicacion.html")

# Ruta para el detalle de un producto con parámetro ID
@app.route("/product/<int:id>")
def product_detail(id):
    return render_template("product_detail.html", product_id=id)





