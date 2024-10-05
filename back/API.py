from flask import Flask, request, jsonify
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from IaMarte import process_csv_for_ia, detect_sismo

app = Flask(__name__)

# Directorios de salida
output_directory = './output/'
result_directory = './Resultados/'
os.makedirs(output_directory, exist_ok=True)
os.makedirs(result_directory, exist_ok=True)

@app.route('/detect_sismo', methods=['POST'])
def detect_sismo_api():
    # Verificar si se subió un archivo
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha subido ningún archivo'}), 400

    file = request.files['file']

    # Guardar archivo CSV temporalmente
    temp_file_path = os.path.join(output_directory, file.filename)
    file.save(temp_file_path)

    # Procesar el archivo CSV
    processed_data = process_csv_for_ia(temp_file_path)

    # Cargar el modelo entrenado
    data_file = './output/detection_catalog_scaled_mars.csv'
    data = pd.read_csv(data_file)
    X = data.drop(columns=['is_sismo_start', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)'])
    y = data['is_sismo_start']

    # Escalar y entrenar el modelo
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    model.fit(X_train, y_train)

    # Detectar sismos y devolver resultados
    processed_data = detect_sismo(model, processed_data, threshold=0.3)
    
    # Guardar resultados en CSV
    output_file = os.path.join(result_directory, 'predictions.csv')
    processed_data.to_csv(output_file, index=False)

    return jsonify({'message': 'Predicciones realizadas', 'output_file': output_file})

if __name__ == '__main__':
    app.run(debug=True)
