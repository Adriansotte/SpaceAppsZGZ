import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadCsvService {
  // Cambiar la URL a tu endpoint correcto
  private apiUrl = 'http://localhost:5000/detect_sismo';

  constructor(private http: HttpClient) { }

  uploadFile(file: File): Observable<any> {
    const formData: FormData = new FormData();
    formData.append('file', file, file.name);

    // No establezcas el Content-Type manualmente
    return this.http.post(this.apiUrl, formData, {
      headers: new HttpHeaders({
        // 'Content-Type': 'multipart/form-data' // Este encabezado no se debe establecer manualmente
      })
    });
  }
}
