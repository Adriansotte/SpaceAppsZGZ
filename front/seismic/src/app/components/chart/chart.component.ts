import { Component } from '@angular/core';
import { MessageService } from 'primeng/api';
import { FileUploadEvent } from 'primeng/fileupload';

@Component({
  selector: 'app-chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss']
})
export class ChartComponent {
  uploadedFiles: File[] = [];

  constructor(private messageService: MessageService) { }

  onUpload(event: FileUploadEvent) {
    // Filtrar archivos que no sean CSV
    const validFiles = event.files.filter(file => file.name.endsWith('.csv'));

    if (validFiles.length === 0) {
      this.messageService.add({ severity: 'error', summary: 'Error', detail: 'Please upload only CSV files.' });
      return; // No se permite subir archivos que no sean CSV
    }

    for (let file of validFiles) {
      this.uploadedFiles.push(file);
    }

    this.messageService.add({ severity: 'info', summary: 'File Uploaded', detail: '' });
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
