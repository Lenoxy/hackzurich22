import { Component } from '@angular/core';
import { Passenger } from './models/passenger.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'hackzurich22-elevator-screen';
  floor: number = 1;
  passengers: Passenger[] = [
    {persNumber: '0001', destinationFloor: 3},
    {persNumber: '0002', destinationFloor: 1},
    {persNumber: '0003', destinationFloor: 2}
  ];
}
