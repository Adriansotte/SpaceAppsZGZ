import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { ChartComponent } from './components/chart/chart.component';
import { EarthComponent } from './components/earth/earth.component';
import { ArtificialComponent } from './components/artificial/artificial.component';

const routes: Routes = [
  {
    path: "",
    component: HomeComponent
  },
  {
    path: "chart",
    component: ChartComponent
  },
  {
    path: "earth",
    component: EarthComponent
  },
  {
    path: "detection",
    component: ArtificialComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
