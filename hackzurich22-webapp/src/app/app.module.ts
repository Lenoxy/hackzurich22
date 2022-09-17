import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DestinationPickerComponent } from './components/destination-picker/destination-picker.component';
import { ApiService } from './services/api.service';
import { HttpClientModule } from '@angular/common/http';
import { WsService } from './services/ws.service';
import { HeaderComponent } from './components/header/header.component';
import { CommonModule } from '@angular/common';
import {TripComponent} from "./components/trip/trip.component";
import { PatientService } from './services/patient.service';

@NgModule({
  declarations: [
    AppComponent,
    DestinationPickerComponent,
    HeaderComponent,
    TripComponent
  ],
  imports: [
    BrowserModule,
    CommonModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [ApiService, WsService, PatientService],
  bootstrap: [AppComponent]
})
export class AppModule { }
