# Week 2 Tute Notes

## Admin
### Presentations
- You can give a 5-10 minute presentation on something cool in web security for bonus marks.
- You can also present walkthroughs for a challenge if you've got a cool solution, no bonus marks though.

### Reports
- Reminder: you should write notes. Even better: take screenshots.

## Content
### Sessions, Tokens and Cookies
- A session is an ongoing conversation with the server.
- A token represents this session in some way.
- This token is provided to the server on every request. Usually via:
  - A particular header like the `Authorization` header or a custom one like `X-Api-Key`.
  - COOKIES!

### Cookies
- Servers set them via the `Set-Cookie` header.
- Browsers see that header, save them, and send them back to the server on every subsequent request.
- Can be easily modified in your browser dev tools.

### Tokens
- Tokens are a method of encoding session information.
- Two main (secure) varieties:
  - Opaque - random value that the server stores in a database/cache. When it receives one from a client, it looks it up to find the corresponding user/information.
  - Signed - the cookie actually stores information about the session (perhaps the JSON `{"user": "HamishWHC"}`), but this data is cryptographically signed so that changes client-side can be noticed.
    - Only the server can issue/modify these tokens, and (typically) only the server can verify them.
- Other insecure forms:
  - Plaintext - cookies might literally be `user=HamishWHC`. Change that client-side to `user=admin` and congrats, you are now an admin.
  - Basic encodings - the same as above, but

### Signed Token Formats
- Flask Sessions
  - Example: `eyJyb2xlIjoiVXNlciIsInVzZXJuYW1lIjoiSGFtaXNoV0hDIn0.ZdLouw.XZ40yxMBU90n4k42pxuBJsI_o1g`
  - The 3 sections are separated by dots. The *first* section contains session data base64 encoded. The above token's data is `{"role":"User","username":"HamishWHC"}`
  - You'll only see these in Flask (Python) apps, but Flask apps are easy to write so they appear in this course a lot.
- JWTs
  - Example: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMzM3IiwibmFtZSI6IkhhbWlzaFdIQyIsImlhdCI6MTUxNjIzOTAyMiwiZXhwIjoxNTE2MjQyNjIyfQ.2LFyhFSEzMzpC3vLOfrOURI6XaL5Brcn-hTRsL6lb88`
  - The 3 sections are separated by dots. The *middle* section contains session data base64 encoded. The above token's data is:
    ```json
    {
        "sub": "1337",
        "name": "HamishWHC",
        "iat": 1516239022,
        "exp": 1516242622
    }
    ```
    - This data is known as the "claims" of the JWT.
    - There is a set of common claims that are often seen on JWTs:
      - `sub`: subject i.e. who the token was issued to
      - `exp`: expiry date (as a UNIX timestamp)
      - `iat`: issued at (as a UNIX timestamp)
      - `aud`: audience i.e. who is expected to receive and verify this
  - The first section is the header and contains signing algorithm info:
    ```json
    {
        "alg": "HS256",
        "typ": "JWT"
    }
    ```
    - `alg` is most commonly `HS156` (HMAC SHA256), but RSA or other signing algorithms can also be used. Sometimes you can even put "none" as the algorithm and just have no signature!
  - JWT is sometimes pronounced "jot".
  - https://jwt.io is your friend.