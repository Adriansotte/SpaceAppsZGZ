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
import { SplitterModule } from 'primeng/splitter';   
import { AccordionModule } from 'primeng/accordion';
import { FormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FooterComponent } from './components/footer/footer.component';
import { GalleriaModule } from 'primeng/galleria';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    ChartComponent,
    EarthComponent,
    ArtificialComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CardModule,
    FileUploadModule,
    TabMenuModule,
    ToastModule,
    BadgeModule,
    SplitterModule,
    AccordionModule,

    BrowserAnimationsModule,
    FormsModule,
    ButtonModule,
    GalleriaModule
  ],
  providers: [MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
