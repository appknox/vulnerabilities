
When using WebView, ensure the following:

- Use WebView to load only trusted content
- Always load resources over HTTPS
- Avoid using Javascript within WebView. If Javascript is absolutely
  required, be sure that each context is escaped properly by using an
  XSS filter component such as the OWASP Java Encoder Project
- Accept only plain-text user input and sanitize it before displaying
  in WebView

