import { Component } from '@angular/core';
import { Passenger } from './models/passenger.model';
import { WsService } from './services/ws.service';
import { ElevatorState } from './types/elevator-state.type';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'hackzurich22-elevator-screen';
  state: ElevatorState = 'unboarding'
  floor: number = 1;
  passengers: Passenger[] = [
    {persNumber: '0001', destinationFloor: 3},
    {persNumber: '0002', destinationFloor: 1},
    {persNumber: '0003', destinationFloor: 2}
  ];

  constructor(private wsService: WsService) {
    this.sendStartMessage();
    wsService.messages.subscribe(msg => {
      console.log(msg);
    })
  }

  sendStartMessage() {
  }

}
