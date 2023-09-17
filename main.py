# Creación de API para guardar datos en archivo .TXT
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/guardar', methods=['POST'])
def guardar_en_txt():
    try:
        data = request.get_json()

        if data:
            with open('datos.txt', 'a') as archivo:
                archivo.write(jsonify(data))
            
            return jsonify({'mensaje': 'Datos guardados correctamente'}), 200
        else:
            return jsonify({'mensaje': 'No se enviaron datos en la solicitud'}), 400

    except Exception as e:
        return jsonify({'mensaje': 'Error al procesar la solicitud', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)