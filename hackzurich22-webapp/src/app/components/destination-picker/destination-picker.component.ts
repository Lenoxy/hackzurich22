import { Component, OnInit } from '@angular/core';
import { Patient } from 'src/app/models/patient.model';
import { ApiService } from 'src/app/services/api.service';
import { WsService } from 'src/app/services/ws.service';
import {Router} from "@angular/router";

@Component({
  selector: 'app-destination-picker',
  templateUrl: './destination-picker.component.html',
  styleUrls: ['./destination-picker.component.scss']
})
export class DestinationPickerComponent implements OnInit {

  constructor(private apiService: ApiService, private wsService: WsService, private router: Router) {
  }

  public errors: string[] = [];
  public name: string = '';
  public patients: Patient[] = [
    {name: 'Max Muster', floor: 3, room: 303}
  ]

  searchPerson() {
    this.router.navigate(['/trip']);
   /* this.errors = [];
    if (!this.name) {
      this.errors.push('Please enter a name.');
    } else {
      if (!this.patients.some(patient => patient.name.toLowerCase() === this.name.toLowerCase())) {
        this.errors.push('The requested person could not be found.')
      } else {
        this.apiService.callElevator(this.patients.find(patient => patient.name.toLowerCase() === this.name.toLowerCase()) as Patient).then(res => {
          console.log(res);
        })
      }
    }*/
  }

  ngOnInit(): void {
  }
}
