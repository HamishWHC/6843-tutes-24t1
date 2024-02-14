# Week 1 Tute Notes
> Maybe in later weeks I'll have slides. I've been focused on infra.

## Admin
### DBAD + Scope
TLDR: Don't be a dick.
This includes anything affecting others' learning.

https://sec.edu.au/good-faith-policy

### whoami
- Hi, I'm Hamish.
- hamish.cox@unsw.edu.au
- @HamishWHC on Discord (and just about everywhere else)

### Course Discussion
- Ed Forums (see WebCMS3 for link)
- https://secso.cc/discord (#comp6443-6843) for memes

### Some Admin
- Tutes aren't compulsory.
- Tutes aren't recorded.
- These notes/resources are on GitHub (and maybe later my website): https://github.com/HamishWHC/6843-tutes-24t1

### Who are you?
- Name, degree, year?
- Why are you doing this course?

### Assessment
- Wargames (10%)
- 2x Reports (40%)
- Midterm (0%, kinda)
- Final (50%)
  - final exam mark = max(final part A, midterm) + part b + part c
- If you have questions on this ask on Ed.

### Wargames
- Due the Sunday (11:59pm) after they release (e.g. challenges released week 1 Monday will be due at 11:59pm on week 2 Sunday).
- Don't leave until the last day to start!
- Collaboration is fine, but you will need to individually submit flags.
- If you are getting frustrated, step away and come back the next day.

### Reports
- Groups of 3, we'll form them next week.
- Keep notes about how you find flags! You do not want to have to re-solve the challenges from scratch when writing the report!
  - Consider also making notes about how you might fix the vulnerability - this is something we want to see in the report.

## Content
### Setup
- See WebCMS: https://webcms3.cse.unsw.edu.au/COMP6443/24T1/resources/95276
- WTF is Burp? Demo.

### Recon
- Your first steps for any challenge/engagement.
- Information gathering:
  - Visiting the website. Understand what it's doing during normal use before trying to exploit it.
  - Looking at its' source code (HTML, JS, maybe the backend source if available) - [sometimes there's just data there](https://www.malwarebytes.com/blog/news/2022/02/journalist-wont-be-indicted-for-hacking-for-viewing-a-state-websites-html).
  - Common files, directories, subdomains, etc. Sometimes you might bruteforce these.
  - Testing weird inputs (later weeks).
- Why?
  - Defenders have to defend *everything*.
  - Attackers just have to find one entry point.
  - So you should expand your search space as much as possible.

### Bruteforcing
- What might you bruteforce?
  - Subdomains: `XYZ.example.com`, tools like Subbrute.
  - Files/directories: `/XYZ`, tools like gobuster.
  - Ports: `example.com:1234`, tools like nmap.
- Demo of subdomain bruteforce.
- You need a wordlist for bruteforcing, I recommend SecLists' as a starting point: https://github.com/danielmiessler/SecLists
- Generally we won't waste your time asking you to bruteforce except for week 1.
  - But if there is a way to narrow down the search space to something more reasonable, then you should try.
  - e.g. /post/1, /post/2, /post/3, etc. is something you should try.
- Be careful in real engagements, bruteforcing can be very noisy or even bring down servers.

### Scripting
- Some challenges require you to write a script to automate some actions (e.g. writing a bruteforcing script).
- To do this, I'd recommend Python + requests, which is a library for sending HTTP requests.
- You should proxy your requests through Burp so that it uses mTLS. Here's a snippet to get started (it's also on WebCMS):
  ```python
  import requests
  from requests.packages.urllib3.exceptions import InsecureRequestWarning
  # Silences warnings about not verifying Burp's CA certificate.
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

  s = requests.session() # This session object saves our settings for the lifetime of the script.
  s.verify = False # Skip trying to verify TLS certs, due to Burp's CA.
  s.proxies = {"https": "http://127.0.0.1:8080"} # Proxy requests through Burp.

  r = s.get("https://whoami.quoccabank.com") # Send a GET request to whoami.
  print(r.content) # b"Hi HamishWHC! Here's a flag: COMP6443{hi_im_HamishWHC_hwOk6dGApTnDudlmsKl-}"
  ```

## What now?
Go setup your certs + Burp (if you haven't already), and get started doing some recon.