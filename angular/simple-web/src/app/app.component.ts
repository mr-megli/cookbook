import { Component } from '@angular/core';
import { BackendService, ResultItem } from './backend.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  result$?: Observable<ResultItem[]>;
  constructor(private readonly backend: BackendService) { }
  search(searchTerm: string) {
    this.result$ = this.backend.search(searchTerm);
  }
}
