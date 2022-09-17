import { Injectable } from "@angular/core";
import { map, Observable, Observer } from "rxjs";
import { AnonymousSubject, Subject } from "rxjs/internal/Subject";
import { environment } from "src/environments/environment";
import { Order } from "../models/order.model";
import { Patient } from "../models/patient.model";
import { PatientService } from "./patient.service";

@Injectable({
  providedIn: 'root'
})
export class WsService {
  private wsId: string = '';
  private wsUrl = `${environment.wsApiUrl}/smartphone`
  private subject: AnonymousSubject<MessageEvent> | undefined;
  public messages: Subject<Order> | undefined;

  public setWsId(id: string) {
    this.wsId = id;
  }

  public getWsId(): string {
    return this.wsId;
  }

  constructor(private patientService: PatientService) {
  }

  public connect(url: string): AnonymousSubject<MessageEvent> {
    if (!this.subject) {
      this.subject = this.create(url);
    }
    return this.subject;
  }

  private create(url: string): AnonymousSubject<MessageEvent> {
    let ws = new WebSocket(url);
    let observable = new Observable((obs: Observer<MessageEvent>) => {
      ws.onmessage = obs.next.bind(obs);
      ws.onerror = obs.error.bind(obs);
      ws.onclose = obs.complete.bind(obs);
      ws.onopen = () => {
        const patient = this.patientService.getPatient() as Patient;
        const message: Order = {
          customer_id: this.patientService.getPatientId() as number,
          from_floor: 0,
          to_floor: patient.floor
        };
        (this.messages as Subject<Order>).next(message);
      }
      return ws.close.bind(ws);
    })
    observable.subscribe();
    let observer = {
      error: null,
      complete: null,
      next: (data: Object) => {
        if (ws.readyState === WebSocket.OPEN) {
          ws.send(JSON.stringify(data))
        }
      }
    }
    return new AnonymousSubject<MessageEvent>(observer as unknown as Observer<MessageEvent<any>>, observable)
  }
}
