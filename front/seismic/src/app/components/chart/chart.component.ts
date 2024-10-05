import { Component } from '@angular/core';
import { MessageService } from 'primeng/api';
import { FileUploadEvent } from 'primeng/fileupload';
import { UploadCsvService } from 'src/app/services/upload/upload-csv.service';

@Component({
  selector: 'app-chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss']
})
export class ChartComponent {
  uploadedFiles: File[] = [];
  imagePaths: string[] = [];  // Aquí almacenaremos las rutas de las imágenes
  loading: boolean = false; // Nuevo estado para controlar el spinner

  constructor(
    private messageService: MessageService,
    private uploadCsvService: UploadCsvService
  ) { }

  onUpload(event: FileUploadEvent) {
    // Filtrar archivos que no sean CSV
    const validFiles = event.files.filter(file => file.name.endsWith('.csv'));

    if (validFiles.length === 0) {
      this.messageService.add({ severity: 'error', summary: 'Error', detail: 'Please upload only CSV files.' });
      return; // No se permite subir archivos que no sean CSV
    }

    this.loading = true; // Activar el spinner

    // Subir archivos válidos
    validFiles.forEach(file => {
      this.uploadCsvService.uploadFile(file).subscribe(
        response => {
          // Almacena el archivo subido en el array de archivos subidos
          this.uploadedFiles.push(file);

          // Manejar la respuesta del servidor
          if (response.message) {
            this.messageService.add({ severity: 'info', summary: 'File Uploaded', detail: response.message });
          } else {
            this.messageService.add({ severity: 'info', summary: 'File Uploaded', detail: 'Upload successful!' });
          }

          // Recoger la lista de imágenes desde la respuesta
          if (response.image_paths) {
            this.imagePaths = response.image_paths.map((path: string) => {
              return `/assets/${path}`;  // Construir la ruta completa de las imágenes
            });
            console.log('Image Paths:', this.imagePaths);
          }
        },
        error => {
          this.messageService.add({ severity: 'error', summary: 'Upload Failed', detail: error.error?.message || 'An error occurred during upload.' });
        },
        () => {
          this.loading = false; // Desactivar el spinner después de completar la carga
        }
      );
    });
  }

  formatSize(bytes: number): string {
    const k = 1024;
    const sizes = ['bytes', 'KB', 'MB', 'GB'];

    if (bytes === 0) return '0 bytes';

    const i = Math.floor(Math.log(bytes) / Math.log(k));
    const formattedSize = parseFloat((bytes / Math.pow(k, i)).toFixed(2));

    return `${formattedSize} ${sizes[i]}`;
  }
}
