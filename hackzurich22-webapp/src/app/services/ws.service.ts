import { Injectable } from "@angular/core";

@Injectable({
  providedIn: 'root'
})
export class WsService {
  private wsId: string = '';

  public setWsId(id: string) {
    this.wsId = id;
  }

  public getWsId(): string {
    return this.wsId;
  }
}
