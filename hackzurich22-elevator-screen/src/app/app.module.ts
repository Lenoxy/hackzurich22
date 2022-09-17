import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WsService } from './services/ws.service';
import { ElevatorScreenComponent } from './components/elevator-screen/elevator-screen.component';
import { InsideScreenComponent } from './components/inside-screen/inside-screen.component';
import { OutsideScreenComponent } from './components/outside-screen/outside-screen.component';

@NgModule({
  declarations: [
    AppComponent,
    ElevatorScreenComponent,
    InsideScreenComponent,
    OutsideScreenComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [WsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
