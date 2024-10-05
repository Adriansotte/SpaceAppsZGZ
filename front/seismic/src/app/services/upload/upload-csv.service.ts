import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadCsvService {
  private apiUrl = 'http://localhost:5000/upload'; // Cambia esto a tu URL de backend

  constructor(private http: HttpClient) { }

  uploadFile(file: File): Observable<any> {
    const formData: FormData = new FormData();
    formData.append('file', file, file.name);
    console.log(formData)
    return this.http.post(this.apiUrl, formData, {
      headers: new HttpHeaders({
        // 'Content-Type': 'multipart/form-data' // Este encabezado no se debe establecer manualmente
      })
    });
  }
}
