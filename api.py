from flask import Flask, request, jsonify
from utils.getData import getData
app = Flask(__name__)



@app.route('/api', methods=['POST'])
def recibir_datos():
    try:
        data = request.get_json()  # Obtener los datos en formato JSON
    except Exception as e:
        print("Error al obtener los datos:", e)
        return jsonify({"error": "Error al obtener los datos"}), 400

    if not data or 'cuil' not in data or 'password' not in data or 'fecha_desde' not in data:
        return jsonify({"error": "Faltan parámetros"}), 400

    data = getData(data['cuil'], data['password'], data['fecha_desde'])

    return jsonify({"mensaje": "Datos recibidos", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

