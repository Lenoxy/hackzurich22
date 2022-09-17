import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DestinationPickerComponent } from './components/destination-picker/destination-picker.component';
import { ApiService } from './services/api.service';
import { HttpClientModule } from '@angular/common/http';
import { WsService } from './services/ws.service';

@NgModule({
  declarations: [
    AppComponent,
    DestinationPickerComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [ApiService, WsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
