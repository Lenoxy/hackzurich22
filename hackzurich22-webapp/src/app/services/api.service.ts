import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Patient } from "../models/patient.model";
import { environment } from '../../environments/environment';
import { PatientService } from "./patient.service";
import { WsService } from "./ws.service";
import {map, Subject } from "rxjs";
import { Order } from "../models/order.model";

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient, private patientService: PatientService, private wsService: WsService) {
  }


  public callElevator(patient: Patient): Promise<string> {
    return new Promise<string>((resolve => {
      this.http.post(`${environment.apiUrl}/ride/new`, {
        'from_floor': 0,
        'to_floor': patient.floor,
        'room': patient.room
      }).forEach(res => {
        this.patientService.setPatient(patient);
        this.patientService.setPatientId(res as number);
        this.wsService.messages = <Subject<Order>>this.wsService.connect(`${environment.wsApiUrl}/smartphone`).pipe(
          map(
            (response: MessageEvent): Order => {
              let data = JSON.parse(response.data)
              return data;
            }
          )
        )
        resolve(res as string);
      }).catch(error => console.log(error))
    }))
  }
}

