import { Injectable } from "@angular/core";
import {map, Observable, Observer } from "rxjs";
import { AnonymousSubject, Subject } from "rxjs/internal/Subject";
import { Message } from "../models/message.model";


@Injectable({
  providedIn: 'root'
})
export class WsService {
  private  wsUrl = 'ws://localhost:3000/' // ??
  private subject: AnonymousSubject<MessageEvent> | undefined;
  public messages: Subject<Message>;

  constructor() {
    this.messages = <Subject<Message>>this.connect(this.wsUrl).pipe(
      map(
        (response: MessageEvent): Message => {
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
