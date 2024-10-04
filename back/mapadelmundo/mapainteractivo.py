# Importamos las librerías necesarias
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import json

# Cargamos los Datos del CSV
url = r'back\mapadelmundo\database.csv'
earthquakes = pd.read_csv(url)

# Convertimos la columna 'Date' a un formato de fecha adecuado
earthquakes['Date'] = pd.to_datetime(earthquakes['Date'], format='%d/%m/%Y', errors='coerce')

# Normalizamos la columna 'Type'
earthquakes['Type'] = earthquakes['Type'].str.lower().str.strip()

# Filtramos solo terremotos
earthquakes = earthquakes[earthquakes['Type'] == 'earthquake']

# Eliminamos filas con datos faltantes
earthquakes = earthquakes.dropna(subset=['Latitude', 'Longitude', 'Magnitude', 'Date'])

# Filtramos los terremotos con magnitud mayor o igual a 7
earthquakes = earthquakes[earthquakes['Magnitude'] >= 7]

# Creamos el mapa inicial centrado en la media de latitud y longitud
m = folium.Map(location=[earthquakes['Latitude'].mean(), earthquakes['Longitude'].mean()], zoom_start=2)

# Convertimos la columna 'Date' a string para que sea serializable a JSON
earthquakes['Date'] = earthquakes['Date'].dt.strftime('%Y-%m-%d')

# Guardamos los datos en un archivo JavaScript para que se procesen luego en el HTML
earthquake_data = earthquakes[['Latitude', 'Longitude', 'Magnitude', 'Date', 'Depth']].to_dict(orient='records')

# Creamos el archivo .js con los datos de terremotos en formato JSON
with open(r'back\mapadelmundo\earthquake_data.js', 'w') as f:
    f.write(f"var earthquakeData = {json.dumps(earthquake_data)};")