import { Component } from '@angular/core';
import { MessageService } from 'primeng/api';
import { FileUploadEvent } from 'primeng/fileupload';
import { DetectService } from 'src/app/services/detect/detect.service';

@Component({
  selector: 'app-artificial',
  templateUrl: './artificial.component.html',
  styleUrls: ['./artificial.component.scss']
})
export class ArtificialComponent {

  uploadedFiles: File[] = [];
  imagePaths: string[] = [];  // Aquí almacenaremos las rutas de las imágenes
  loading: boolean = false; // Nuevo estado para controlar el spinner
  sismoDate: Date | null = null; // Nueva variable para almacenar la fecha del sismo

  constructor(
    private messageService: MessageService,
    private detectService: DetectService
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
      this.detectService.uploadCSV(file).subscribe(
        response => {
          this.loading = false; // Desactivar el spinner
          console.log('Respuesta del servidor:', response); // Printear la respuesta en la consola

          // Asegúrate de que `response` contiene las propiedades esperadas
          if (response.first_time_abs) {
            // Convertir la fecha a un objeto Date
            this.sismoDate = new Date(response.first_time_abs);
          } else {
            this.sismoDate = null; // No se encontraron datos suficientes para calcular el tiempo del sismo
          }

          // Manejar mensajes de éxito de la subida
          if (response.message) {
            this.messageService.add({ severity: 'info', summary: 'File Uploaded', detail: response.message });
          } else {
            this.messageService.add({ severity: 'info', summary: 'File Uploaded', detail: 'Upload successful!' });
          }

          // Si la respuesta incluye imágenes, puedes hacer algo como esto
          if (response.image_paths) {
            this.imagePaths = response.image_paths.map((path: string) => {
              return `/assets/${path}`;  // Construir la ruta completa de las imágenes
            });
          }
        },
        error => {
          this.loading = false; // Desactivar el spinner en caso de error
          this.messageService.add({ severity: 'error', summary: 'Upload Failed', detail: error.error?.message || 'An error occurred during upload.' });
          console.error('Error en la subida del archivo:', error); // Printear el error en la consola
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
