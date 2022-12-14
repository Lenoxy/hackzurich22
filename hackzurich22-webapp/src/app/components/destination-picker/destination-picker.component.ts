import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Patient } from 'src/app/models/patient.model';
import { ApiService } from 'src/app/services/api.service';
import { WsService } from 'src/app/services/ws.service';

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
    {name: 'Rosmarie Meier', floor: 3, room: 303}
  ]

  searchPerson() {
   this.errors = [];
    if (!this.name) {
      this.errors.push('Please enter a name.');
    } else {
      if (!this.patients.some(patient => patient.name.toLowerCase() === this.name.toLowerCase())) {
        this.errors.push('The requested person could not be found.')
      } else {
        this.apiService.callElevator(this.patients.find(patient => patient.name.toLowerCase() === this.name.toLowerCase()) as Patient).then(res => {
          this.router.navigate(['/trip']);
        })
      }
    }
  }

  ngOnInit(): void {
  }
}
