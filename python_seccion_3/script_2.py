from flask import Flask, jsonify, request
import json
import logging

app = Flask(__name__)

# Creamos la configuración de los logs
logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Cargamos los datos desde el archivo JSON
def cargar_datos():
    try:
        with open("ventas_diarias.json", "r") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error al cargar datos: {e}")
        return []

@app.route("/ventas", methods=["GET"])
def obtener_ventas():
    producto = request.args.get("producto")
    datos = cargar_datos()
    
    if producto:
        datos = [d for d in datos if d["producto"] == producto]
    
    if not datos:
        return jsonify({"mensaje": "No hay datos disponibles"}), 404
    
    return jsonify(datos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)