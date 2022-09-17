import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {
  }


  public callElevator(): Promise<string> {
    return new Promise<string>((resolve => {
      this.http.post('http://localhost:3000/new', {})
    }))
  }
}
