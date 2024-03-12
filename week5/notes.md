# Week 5
## Admin
### Midterm is over!
* What did you think?
* How do you feel you went?
* Do you want me to go through it?

## Content
### Advanced SQLi
* See demo from last week.
* `UNION`s
* WAFs

### RCE
* Any time you can execute code *of your choice* on a remote server.
* Often referred to as a shell.
* Common methods:
  * Server-Side Template Injection
  * Command Injection
  * Local File Inclusion

### SSTI
* To be able to display different HTML based on e.g. the user, post content, etc we need to be able to template HTML.
* e.g.
  ```html
  <p>Hello {{username}}!</p>
  ```
* What if the template itself contains user input?
  * e.g. the template can be specified by a user as part of a 'plugin' system or similar.
* Demo.

### Command Injection
* Sometimes a web app runs a command to do something by running a program.
* Often, user input needs to be included as part of the command.

### Local File Inclusion
* Extension to Local File Disclosure and/or Path Traversal.
* Often the path you include is interpreted as code instead of just being treated as text.

### Reverse Shells
* A way of getting a nice shell to work with rather than some weird SSTI/Command Injection/LFI payload.
* See https://revshells.com