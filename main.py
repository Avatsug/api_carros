from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta que manejará las solicitudes POST para guardar carros
@app.route('/guardar_carro', methods=['POST'])
def guardar_carro():
    try:
        # Obtén los datos del carro desde la solicitud POST
        data = request.get_json()

        # Verifica si se enviaron datos válidos
        if "marca" in data and "color" in data and "estado" in data:
            # Guarda los datos del carro en el archivo carros.txt
            with open('carros.txt', 'a') as archivo:
                archivo.write(f"{data['marca']},{data['color']},{data['estado']}\n")
            
            return jsonify({'mensaje': 'Carro guardado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Datos de carro incompletos en la solicitud'}), 400

    except Exception as e:
        return jsonify({'mensaje': 'Error al procesar la solicitud', 'error': str(e)}), 500

# Ruta que manejará las solicitudes GET para obtener carros
@app.route('/obtener_carros', methods=['GET'])
def obtener_carros():
    try:
        # Leer los carros guardados desde el archivo carros.txt
        carros = []
        with open('carros.txt', 'r') as archivo:
            for linea in archivo:
                marca, color, estado = linea.strip().split(',')
                carros.append({'marca': marca, 'color': color, 'estado': estado})
        
        return jsonify({'carros': carros}), 200

    except Exception as e:
        return jsonify({'mensaje': 'Error al obtener carros', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)