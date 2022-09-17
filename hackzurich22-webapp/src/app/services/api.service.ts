import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Patient } from "../models/patient.model";
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {
  }


  public callElevator(patient: Patient): Promise<string> {
    return new Promise<string>((resolve => {
      this.http.post(`${environment.apiUrl}/ride/new`, {
        'from_floor': 0,
        'to_floor': patient.floor,
        'room': patient.room
      }).forEach(res => {
        resolve(res as string);
      }).catch(error => console.log(error))
    }))
  }
}

