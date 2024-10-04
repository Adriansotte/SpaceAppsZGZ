# Importamos las librerías necesarias
import pandas as pd
import folium

# Cogemos los Datos
url = 'back\mapadelmundo\earthquakes.csv'
earthquakes = pd.read_csv(url)

# Escogemos solo los datos necesarios
earthquakes = earthquakes.dropna(subset=['location', 'magnitude','name','year'])

# Función para limpiar y extraer latitud y longitud de los datos de location
def extract_coordinates(location):
    location = location.replace('POINT', '').replace('(', '').replace(')', '')
    lon, lat = location.split()
    return float(lon), float(lat)

earthquakes['longitude'], earthquakes['latitude'] = zip(*earthquakes['location'].apply(extract_coordinates))

# Ordenamos los terremotos por magnitud en orden descendente y luego lo limitamos a 500
earthquakes = earthquakes.sort_values(by='magnitude', ascending=False)
earthquakes_limited = earthquakes.head(100)

# Muestra en consola de que están las magnitudes
print(earthquakes_limited[[ 'latitude', 'longitude', 'magnitude', 'name', 'year']].head(10))

# Creamos un mapa centrado en el promedio de las coordenadas
m = folium.Map(location=[earthquakes_limited['latitude'].mean(), earthquakes_limited['longitude'].mean()], zoom_start=2)

# Agregamos marcadores para cada terremoto
for idx, row in earthquakes_limited.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Magnitude: {row['magnitude']}<br>Year: {row['year']} <br> {row['name']}",
        icon=folium.Icon(color='red')
    ).add_to(m)

# Guardamos el mapa como un archivo HTML
m.save('back\mapadelmundo\mapa_terremotos.html')

# Para visualizar el mapa en Jupyter Notebook, puedes usar:
m