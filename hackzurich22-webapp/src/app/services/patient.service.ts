import { Injectable } from "@angular/core";
import { Patient } from "../models/patient.model";

@Injectable({
  providedIn: 'root'
})
export class PatientService {
  private patient: Patient | undefined;
  private patientId: number | undefined;

  public setPatient(patient: Patient) {
    this.patient = patient;
  }

  public setPatientId(patientId: number) {
    this.patientId = patientId;
  }

  public getPatient(): Patient |undefined {
    return this.patient;
  }

  public getPatientId(): number | undefined {
    return this.patientId;
  }
 }
