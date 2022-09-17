import { Component, OnInit } from '@angular/core';
import { WsService } from 'src/app/services/ws.service';

@Component({
  selector: 'app-trip',
  templateUrl: './trip.component.html',
  styleUrls: ['./trip.component.scss']
})
export class TripComponent implements OnInit {

  constructor(private wsService: WsService) { }

  ngOnInit(): void {
    console.log(this.wsService.getWsId());
  }

}
