# Week 3 Tute Notes

## Admin
### DBAD
This week this is especially important.

### Reports
Any questions about them? They are due end of Week 5.
SAMPLE REPORT.

### Midterm
* 5-6 questions.
  * Authentication vulns
  * Authorisation vulns
  * IDOR
  * Easy SQLI (advanced SQLI is in the lecture afterwards)
  * SSRF
  * Path traversal
* Next Monday 6-7pm.
* Can be used as your Part A mark in the final.
  * Final Exam Mark = MAX(Midterm, Part A) + Part B + Part C
* We will be continuing with the lecture afterwards from 7-9pm.
* You are welcome to come sit in the lecture theatre to do the exam, so you are then at the lecture.

## Content
### What is a server-side vulnerability?
* Anything that affects or exploits an implementation detail of the server's code.
* Some of what we've seen so far (e.g. missing JWT verification) is server-side.
* But we are no longer bypassing a security control like authn/authz, but instead trying to gain access to files, databases or a shell.

### Structured Query Language (SQL)
* Language for querying databases.
  * Not the only database query language, there are also NoSQL servers like MongoDB that do everything using JSON.
* A couple different server options, with their own quirks:
  * MySQL
  * PostgreSQL - also known just as Postgres
  * Microsoft SQL - also known just as SQL Server, which is just confusing
  * SQLite
  * More...
* SQL databases are effectively massive Excel spreadsheets with strict schemas.
* SQL queries/statements end in a semi-colon (`;`).
* You can comment out the remainder of a query with `--`.
* Above all else: GOOGLE THE SYNTAX!
  * Some servers allow `#` as well as `--` to comment.
  * Some require a space after `--` to make it a comment.
* Common statements:
  * `SELECT <column1>, <column2>, ... FROM <table> ...;`
    * `WHERE <condition>`
    * `ORDER BY <column> [ASC|DESC]`
    * `LIMIT <x> OFFSET <y>` - returns only `x` rows
    * May also be `SELECT * FROM <table>` to select every column.
  * `INSERT INTO <table> (<column1>, <column2>) VALUES (<value_for_column1>, <value_for_column2>, ...);`
  * `UPDATE <table> SET (<column1> = <value_for_column1>, <column2> = <value_for_column2>, ...) WHERE <condition>;`
  * `DELETE FROM <table> WHERE <condition>;`
* Demo using `chinook.db` from https://www.sqlitetutorial.net/sqlite-sample-database/.
* How is this done in code?
* Sometimes, you see this: 
  ```python
  cursor.execute("SELECT * FROM users WHERE email='" + username + "' AND password='" + password_hash + "'")
  ```

### SQL Injection (SQLI)
* If we have the following query: `SELECT * FROM users WHERE username='<username>' AND password_hash='<password_hash>';`
* What happens if we enter the username `'`?
* The query becomes `SELECT * FROM users WHERE username=''' AND password_hash='abcdef';` (note that the password is a hash so the user can't control the input there).
* This is no longer valid SQL, since we have unmatched quotes.
* Can we construct a query together that will allow us to login without giving a valid password?
* Demo, courtesy of Andrew: https://github.com/featherbear/demo-sqli
* How code *should* use SQL:
  ```python
  # It'll depend on the DB library you are using, always read it's documentation.
  # This is how it should be done in pymysql.
  cursor.execute("SELECT * FROM users WHERE email='%s' AND password='%s'", (username, password_hash))
  ```
* In a real engagement, avoid extracting data if possible - do stuff like `SELECT 1;` or `SELECT COUNT(*) FROM <table>;`.

### Server-Side Request Forgery (SSRF)
* Often, servers need to go access something from the internet.
* Also often, these somethings are specified by the user.
* e.g. Profile pictures, file fetching, link previews.
* If you get a server to request something you control, you can get information or extract data.
* If you get a server to request something you can't access, but it can, you've bypassed their security and can make simple HTTP requests within their network.

### Path Traversal and Local File Disclosure (LFD)
* In a similar sense, servers often need to access something on their filesystem.
* Also often, these somethings are specified by the user.
* e.g. Profile pictures, page contents.
* If you get a server to access a file outside of where it should, you can potentially read arbitrary files on the filesystem.

### Other Server-Side Vulnerabilities
* RCE
  * Any time you can execute code *of your choice* on a remote server.
  * Often referred to as a shell. Reverse shells in particular are cool and we will discuss them next week.
  * Common methods:
    * Server-Side Template Injection
    * Command Injection
    * Local File Inclusion
* NoSQL Injection - injection into those NoSQL databases I mentioned.
* I will talk about these more next week.
* The challenges for them are up already.
* I can talk about them now if you would like, but I haven't got notes ready.