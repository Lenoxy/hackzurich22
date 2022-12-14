import { Injectable } from "@angular/core";
import {map, Observable, Observer } from "rxjs";
import { AnonymousSubject, Subject } from "rxjs/internal/Subject";
import { Message } from "../models/message.model";
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class WsService {
  private  wsUrl = `${environment.wsApiUrl}/elevator` // ??
  private subject: AnonymousSubject<MessageEvent> | undefined;
  public messages: Subject<string>;

  constructor() {
    this.messages = <Subject<string>>this.connect(this.wsUrl).pipe(
      map(
        (response: MessageEvent): string => {
          let data = JSON.parse(response.data)
          return data;
        }
      )
    )
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
        const message = 'A'
        this.messages.next(message);
      }
      return ws.close.bind(ws);
    })
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
