# Importamos las librerías necesarias
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

#Cojemos Los Datos
url = 'C:\\Users\\David\\Desktop\\hackaton\\earthquakes.csv'
earthquakes = pd.read_csv(url)

# Escogemos solos los datos necesarios
earthquakes = earthquakes.dropna(subset=['location', 'magnitude'])

# Función para limpiar y extraer latitud y longitud de los datos de location
def extract_coordinates(location):
    location = location.replace('POINT', '').replace('(', '').replace(')', '')
    lon, lat = location.split()
    return float(lon), float(lat)

earthquakes['longitude'], earthquakes['latitude'] = zip(*earthquakes['location'].apply(extract_coordinates))

# Ordenamos los terremotos por magnitud en orden descendente y luego lo limitamos a 500
earthquakes = earthquakes.sort_values(by='magnitude', ascending=False)

earthquakes_limited = earthquakes.head(500)

# Muestra en consola de que estan las magnitudes
print(earthquakes_limited[['latitude', 'longitude', 'magnitude']].head(10))

# Convertimos el DataFrame limitado a un GeoDataFrame
geometry = [Point(xy) for xy in zip(earthquakes_limited['longitude'], earthquakes_limited['latitude'])]
geo_df = gpd.GeoDataFrame(earthquakes_limited, geometry=geometry)

# Mapa Del Mundo
shapefile_path = r'C:\\Users\\David\\Desktop\\hackaton\\ne_110m_admin_0_countries.shp'
world = gpd.read_file(shapefile_path)

#Ejes
fig, ax = plt.subplots(figsize=(15, 10))

#Creamos el mapa
world.plot(ax=ax, color='lightblue', edgecolor='black')

# Dibujamos los puntos de los terremotos en rojo si hay puntos en el GeoDataFrame
if not geo_df.empty:
    geo_df.plot(ax=ax, marker='o', color='red', markersize=5, label='Terremotos')
    plt.legend()
else:
    print("El GeoDataFrame está vacío, no hay puntos para mostrar.")

plt.title('Mapa de los 500 Terremotos con Mayor Magnitud')

plt.show()