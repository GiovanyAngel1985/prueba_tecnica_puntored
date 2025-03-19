import pymysql
import json
from datetime import datetime, timedelta

# Generamos la configuración de conexión a RDS
DB_CONFIG = {
    "host": "rds-endpoint",
    "user": "my-user",
    "password": "contraseña",
    "database": "name-database"
    }

# Fijamos la fecha del día anterior
fecha_inicio = (datetime.today() - timedelta(days = 1)).strftime('%Y-%m-%d')

# Consulta SQL para extraer la info de la DB
QUERY = """
SELECT
    v.fecha,
    c.id AS cliente_id,
    c.nombre,
    c.apellido,
    COUNT(v.id) AS transacciones,
    SUM(v.monto) AS monto_total,
    v.producto
FROM ventas v
JOIN clientes c ON v.cliente_id = c.id
WHERE v.fecha = %s
GROUP BY v.fecha, c.id, c.nombre, c.apellido, v.producto
"""

# Función para extraer datos

def extraer_datos():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(QUERY, (fecha_inicio))
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos
    except Exception as e:
        print(f"Error al extraer datos: {e}")
        return []

# Ahora guardamos los datos en un archivo JSON

def guardar_json(datos, nombre_archivo="ventas_diarias.json"):
    with open(nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4)

if __name__ == "__main__":
    datos = extraer_datos()
    guardar_json(datos)
    print("Datos extraídos y guardados en ventas_diarias.json")