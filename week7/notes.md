# Week 7
## Admin
### Challenges so far
* Any walkthroughs?
* GCC, Lookup, Secrets...?

## Content
### Cross Site Scripting (XSS)
* Spelt with an X (a cross) because CSS was taken.
* Effectively JS injection - same idea as SQL injection.
* e.g. Say you have a website that is generating the following HTML using some templating language like Jinja2:
  ```html
  <h1>Hello {{username}}!</h1>
  ```
  Suppose that `username` is set to `<script>alert(1)</script>`. What does the HTML end up as?
* What can we do with this?
  * `window.location=...`
  * `fetch("...")`
* Other payload options:
  * `<img src=x onerror="alert(1)">`
  * `<style onload="alert(1)"></style>`
* Can also inject into attributes.
* Some simple defenses:
  * `HttpOnly` cookies
  * WAFs: similar to SQLi, developers will do things like removing `<script>` from any user input and think that will work. You'll just have to experiment.
    * Sometimes `alert(1)` itself is blocked, so you may want to use an alternative for your testing.
  * Most common libraries that do HTML generation will escape HTML characters - including the library I used for the demo but I told it to be insecure for demo purposes. This is usually what has prevented XSS up until now in this course.
* There are more advanced defenses that protect users/sites even after you have managed to get malicious JavaScript onto the page. We will be discussing those after the next lecture (Week 9).

### Cross Site Request Forgery (CSRF)
* XSS payloads can do anything JavaScript can do.
* What if we send a POST request to another website?
* e.g. a POST request to https://realbank.com/transfer that will transfer a user's money?
* If a browser has cookies for a website, it *will*\* send them on every request to that website, so realbank.com will believe the user is logged in and transfer the money.
* Defending against this is a pain, and we will get into it after the next lecture.

### Clickjacking
* Demo