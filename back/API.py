from flask import Flask, request, jsonify
import os
from IaMarte import process_csv_for_ia
from flask_cors import CORS
from PruebaComplicada import process_seismic_data_from_csv

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app)

# Directorios de salida
output_directory = './output/'
result_directory = './Resultados/'
os.makedirs(output_directory, exist_ok=True)
os.makedirs(result_directory, exist_ok=True)

@app.route('/detect_sismo', methods=['POST'])
def detect_sismo_api():
    print("entra")
    
    # Verificar si se subió un archivo
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha subido ningún archivo'}), 400

    file = request.files['file']

    # Guardar archivo CSV temporalmente
    temp_file_path = os.path.join(output_directory, file.filename)
    file.save(temp_file_path)

    # Procesar el archivo CSV
    processed_data = process_csv_for_ia(temp_file_path)
    print(processed_data)

    # Procesar los datos sísmicos y obtener el directorio y las rutas de las imágenes
    processed_data_path, image_paths = process_seismic_data_from_csv(temp_file_path)
    print(f"Processed data path: {processed_data_path}")
    print(f"Image paths: {image_paths}")

    # Asegúrate de que processed_data_path no es None o vacío
    if processed_data_path is not None:
        # Retornar la ruta procesada y la lista de imágenes
        return jsonify({
            'message': 'Archivo procesado con éxito',
            'processed_data_path': processed_data_path,
            'image_paths': image_paths 
        }), 200
    else:
        return jsonify({'error': 'Error en el procesamiento de datos'}), 500  # Código 500 para errores internos

if __name__ == '__main__':
    app.run(debug=True)
