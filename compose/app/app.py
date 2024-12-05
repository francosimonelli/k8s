from flask import Flask, jsonify
import mysql.connector
from decimal import Decimal

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h1>Bienvenido a la Demo de Docker Compose y Flask!</h1>
        <button onclick="window.location.href='/products'">Trae los datos de la base de datos</button>
        <ul id="product-list"></ul>
    '''

@app.route("/products")
def get_products():
    # Conexión a la base de datos MySQL
    connection = mysql.connector.connect(
        host="mysql-db",  # Nombre del servicio de base de datos en Docker Compose
        user="root",
        password="rootpass",
        database="demo"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products;")  # Consulta SQL a la base de datos
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    for product in products:
        product['price'] = float(product['price']) 



    return jsonify(products)  # Devuelve los productos en formato JSON

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Inicia la aplicación en el puerto 5000

