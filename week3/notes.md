# Week 3 Tute Notes

## Admin
### Reports
Watch the lecture. Any questions?

## Content
### Certificates
- How do we know that a server is who they say they are?
- We trust some set of authorities (see system keychain on macOS).
- They cryptographically sign our certificate, so that we can prove we are the owner of some domain and that they are seeing the right content for that domain.
- TLS handshake has client verify the server's certificate, then transitions to symmetric encryption for speed.
  - Server may also verify a client certificate if required or available (since both sides have a certificate this is called Mutual TLS or mTLS).
- What problem exists here?
  - Kind of solved by Organisation Validated and Extended Validation certificates. But they've dropped off.
- HSTS tells browsers to only access a site over HTTPS, but the browser must connect via HTTP the first time to discover this. HSTS Preload is a way for sites to get their HSTS status installed into the browser itself, making HTTP connections mostly unnecessary (if you ignore old browsers or applications that access the site that aren't a browser).

### TOTP 2FA
- Time-based One Time Passwords
- 

### OAuth
- Reminder: Authorization != Authentication
- OAuth is a standard for AUTHORIZING a service.
- A service asks an identity provider (e.g. Google) to access some resource (e.g. the Google Drive API) on your behalf.
- You can restrict the 'scope' of the access provided.
- Often, OAuth is used for authentication by authorizing the service to access your identity (e.g. access to your email address or user ID).
- Demo (draw.io).
- Diagram of a typical OAuth flow (Authorization Code flow):
  ```mermaid
  sequenceDiagram
    participant User as User's Browser
    participant Service as Some Service<br>(e.g. Canva)
    participant IDP as Identity Provider<br>(e.g. Google)
    participant Resource as Resource Server<br>(e.g. Google Drive API)

    User->>Service: GET /login
    activate Service
    Service-->>User: 302 redirect to identity provider<br>with some 'state' value
    deactivate Service

    User->>IDP: GET /oauth/authorize
    activate IDP
    IDP-->>User: 200 login.html
    deactivate IDP
    User->>IDP: POST /login<br>username=...&password=...
    activate IDP
    IDP-->>User: 200 confirm.html
    deactivate IDP

    note right of User: User confirms they would like the<br>service to have some set of permissions<br>(which may include access to their identity).

    User->>IDP: POST /confirm
    activate IDP
    IDP-->>User: 302 redirect back to service<br>with same state value as before and a code
    deactivate IDP

    User->>Service: GET /callback?state=...&code=...
    activate Service
    Service->>IDP: GET /oauth/token?code=...
    activate IDP
    IDP-->>Service: 200 scoped access token
    deactivate IDP

    note right of Service: Service now has credentials<br>for the resource server.

    Service->>Resource: GET /files<br>Authorization: Bearer <token>
    activate Resource
    Resource-->>Service: 200 {...}
    deactivate Resource

    Service-->>User: 200 Here's all your files: ...
    deactivate Service
  ```
- Cool article about why OAuth is still hard: https://www.nango.dev/blog/why-is-oauth-still-hard
- It's really complicated once you get to the details. e.g. https://auth0.com/docs/get-started/applications/application-grant-types#specification-conforming-grants