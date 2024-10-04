import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { HeaderComponent } from './components/header/header.component';
import { FileUploadModule } from 'primeng/fileupload';
import { CardModule } from 'primeng/card';
import { TabMenuModule } from 'primeng/tabmenu';
import { ToastModule } from 'primeng/toast';
import { BadgeModule } from 'primeng/badge';
import { ChartComponent } from './components/chart/chart.component';
import { EarthComponent } from './components/earth/earth.component';
import { ArtificialComponent } from './components/artificial/artificial.component';
import { MessageService } from 'primeng/api';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    ChartComponent,
    EarthComponent,
    ArtificialComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CardModule,
    FileUploadModule,
    TabMenuModule,
    ToastModule,
    BadgeModule
  ],
  providers: [MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
