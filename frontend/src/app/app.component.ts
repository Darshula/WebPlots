import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  language = 'r';
  code = '';
  iframeUrl: SafeResourceUrl | null = null;
  loading = false;
  title = 'frontend';

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  submitScript() {
    this.loading = true;
    this.iframeUrl = null;

    const endpoint =
      this.language === 'python'
        ? 'http://127.0.0.1:65535/python_runner'
        : 'http://127.0.0.1:65535/r_runner';

    this.http.post<any>(endpoint, { code: this.code }).subscribe({
      next: (res) => {
        if (res.file_url) {
          const fullUrl = 'http://127.0.0.1:65535' + res.file_url;
          this.iframeUrl = this.sanitizer.bypassSecurityTrustResourceUrl(fullUrl);
        }
        this.loading = false;
      },
      error: (err) => {
        console.error('Execution error:', err);
        this.iframeUrl = null;
        this.loading = false;
      }
    });
  }
}
