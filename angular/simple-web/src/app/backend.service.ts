import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

export declare interface ResultItem {
  title: string;
  date: number;
}

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private readonly http: HttpClient) { }

  search(searchTerm: string) {
    return this.http.get<ResultItem[]>(`/api/search`, { params: { 'q': searchTerm } });
  }
}
