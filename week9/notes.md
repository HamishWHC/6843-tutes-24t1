# Week 7
## Admin
* Exam is 27th of April/Saturday (ew) Week 11.
* Report is due 24th of April/Wednesday Week 11.
* Report and midterm marks back in an email this week.
* Some general report feedback from Nic:
  * **Order vulnerabilities in order of most to least critical/important.** i.e. start with the RCEs, end with Recon.
  * More details and broader recommendations in remediations would be helpful.
  * Use domains instead of challenge names - the challenges on CTFd are a helpful way for us to assess you finding vulnerabilities and information, **they are not 1:1 to the vulnerabilities that should appear in your report**.
* Some advice for the second report:
  * You do not need to include every vulnerability you find (that would be too much work), **BUT** you *do* need to cover a range of vulnerability classes/exploitation techniques. Cover some XSS, some CSP bypasses, a CSRF, etc.

## Content
### Origins vs Sites
* Origin = Scheme + Full Domain/Hostname + Port
* Site = First Level Private Domain + Public Suffix
  * Public Suffixes are *not* Top Level Domains (e.g. `.com`, `.au`, `.net`, `.xyz`). They may also be known as eTLDs (effective TLDs). The site (as defined above) may be called the eTLD+1.
  * They are any domain under which unaffiliated organisations can register arbitrary domains. e.g. `.com.au` is a public suffix, because any Australian citizen or business can register `<something>.com.au`, and `.nsw.edu.au` is also a public suffix, because any NSW school can register `<something>.nsw.edu.au`.
  * The first level private domain is the first segment after the public suffix.
* e.g. when visiting `https://ctfd.quoccabank.com`, `.com` is the public suffix, `quoccabank` is the first level private domain, so the site/eTLD+1 is `quoccabank.com`, while `https://ctfd.quoccabank.com` (`:443` is implicit due to HTTPS here) is the origin.
* These may occasionally be used interchangably, but they appear in the names of some protections and the distinction is important.

### Same Origin Policy
* One of the first client side security controls.
* Says that a website is only allowed to load content from the same *origin* (with some exceptions).

### CORS
* A set of headers (`Access-Control-Allow-*`) returned by a server that define whether or not scripts on a page are allowed to interact with said server.
* `Access-Control-Allow-Origin` defines the origins that are allowed to interact with the server.
* `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers` define the methods and headers that scripts can use to interact with the server.
* `Access-Control-Allow-Credentials` defines whether or not scripts can tell the browser to send stored cookies alongside the request.
* Demo of SOP + CORS.