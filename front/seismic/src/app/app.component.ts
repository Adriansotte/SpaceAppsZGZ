import { Component } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = "";

  items: MenuItem[] | undefined;

  constructor(private router: Router) { }

  ngOnInit() {
    this.items = [
      { label: 'Home', icon: 'pi pi-home', command: () => this.router.navigate(['']) },
      { label: 'Evalúa tu sismo', icon: 'pi pi-chart-line', command: () => this.router.navigate(['chart']) }, 
      { label: 'Seismos en la tierra', icon: 'pi pi-map-marker', command: () => this.router.navigate(['earth']) }, 
      { label: 'Detección de Seismos', icon: 'pi pi-android', command: () => this.router.navigate(['detection']) }
    ];
  }
}
