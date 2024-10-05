import { Component, OnInit } from '@angular/core';
// Importa los datos de los terremotos
import { earthquakeData } from './earthquake_data';
declare let L: any; // Para que TypeScript reconozca la librería Leaflet

@Component({
  selector: 'app-earth',
  templateUrl: './earth.component.html',
  styleUrls: ['./earth.component.scss']
})
export class EarthComponent implements OnInit {

  filterYear: number = 2000; // Año predeterminado
  map: any;
  markers: any;

  ngOnInit() {
    this.initMap();
    this.addEarthquakesToMap(earthquakeData); // Añadir todos los terremotos al cargar la página
  }

  initMap() {
    // Crear el mapa inicial
    this.map = L.map('map').setView([0, 0], 2);

    // Añadir la capa base del mapa
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(this.map);

    // Crear un grupo de marcadores con clúster
    this.markers = L.markerClusterGroup();
    this.map.addLayer(this.markers);

    // Agregar un marcador de prueba para verificar que el mapa funcione correctamente
    const testMarker = L.marker([34.0522, -118.2437]).bindPopup('Marcador de prueba');
    this.markers.addLayer(testMarker);
  }

  // Función para añadir terremotos al mapa
  addEarthquakesToMap(data: any[]) {
    this.markers.clearLayers(); // Limpiamos el cluster
    data.forEach((earthquake) => {
      if (earthquake.Latitude && earthquake.Longitude) {
        const marker = L.marker([earthquake.Latitude, earthquake.Longitude])
          .bindPopup(
            `Magnitud: ${earthquake.Magnitude}<br>Profundidad: ${earthquake.Depth}<br>Fecha: ${earthquake.Date}`
          );
        this.markers.addLayer(marker);
        console.log(`Marcador agregado en: [${earthquake.Latitude}, ${earthquake.Longitude}]`);
      } else {
        console.warn('Coordenadas no válidas para el terremoto:', earthquake);
      }
    });
  }

  filterByYear() {
    // Validar que el año ingresado esté dentro del rango
    if (this.filterYear < 1965 || this.filterYear > 2016) {
      alert('Por favor, introduce un año entre 1965 y 2016.');
      return; // Salir si el año no es válido
    }

    const filteredData = earthquakeData.filter(earthquake => {
      const year = new Date(earthquake.Date).getFullYear();
      return year === this.filterYear; // Filtrar solo por el año exacto
    });

    console.log('Datos filtrados:', filteredData); // Imprimir datos filtrados
    this.addEarthquakesToMap(filteredData); // Actualizamos el mapa con los datos filtrados
    console.log('Filtrando por año:', this.filterYear, filteredData); // Para verificar el filtrado
  }
}
