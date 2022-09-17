import { Component, OnInit } from '@angular/core';
import { Patient } from 'src/app/models/patient.model';

@Component({
  selector: 'app-destination-picker',
  templateUrl: './destination-picker.component.html',
  styleUrls: ['./destination-picker.component.scss']
})
export class DestinationPickerComponent implements OnInit {

  constructor() {
  }

  public errors: string[] = [];
  public name: string = '';
  public patients: Patient[] = [
    {name: 'Max Muster', floor: 3, room: 303}
  ]

  searchPerson() {
    this.errors = [];
    if (!this.name) {
      this.errors.push('Please enter a name.');
    } else {
      if (!this.patients.some(patient => patient.name.toLowerCase() === this.name.toLowerCase())) {
        this.errors.push('The requested person could not be found.')
      } else {

      }
    }
  }

  ngOnInit(): void {
  }
}
