import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Answer} from "./models/Answer";

@Injectable({
  providedIn: 'root'
})
export class ChatServiceService {

  backendBaseUrl: string = 'http://localhost:5000/'
  constructor(private http: HttpClient) {
  }

  getAnswer(question: string) {


    // return this.http.post<string>(
    //   this.backendBaseUrl + 'process',
    //   {data: question},
    //   {
    //     observe: 'response',
    //   });

    return this.http.post<Answer>(
      this.backendBaseUrl + 'api',
      {question: question, category: "MP"})
      // {responseType: 'text'})

  }

}
