import { Component, Input, OnInit } from '@angular/core';
import { Passenger } from 'src/app/models/passenger.model';
import { WsService } from 'src/app/services/ws.service';
import { ElevatorState } from 'src/app/types/elevator-state.type';

@Component({
  selector: 'app-elevator-screen',
  templateUrl: './elevator-screen.component.html',
  styleUrls: ['./elevator-screen.component.scss']
})
export class ElevatorScreenComponent {
  @Input('is-outside') isOutside: boolean = false;
  state: ElevatorState = 'unboarding'
  floor: number = 0;
  passengers: Passenger[] = [
  ];

  constructor(private wsService: WsService) {
    wsService.messages.subscribe((msg: any) => {
      this.floor = msg.floor || msg.floor === 0 ? msg.floor : this.floor;
      msg.rides.forEach((ride: any) => {
        this.passengers.push({
          persNumber: this.formatCustomerId(ride.customer_id),
          destinationFloor: this.isOutside ? ride.from_floor : ride.to_floor
        })
      })
    })
  }

  private formatCustomerId(id: number): string {
    let idStr: string = id as unknown as string;
    if (id < 10) {
      idStr = '000' + idStr
    } else {
      idStr = '00' + idStr;
    }
    return idStr;
  }

}
