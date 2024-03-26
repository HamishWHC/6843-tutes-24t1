import * as Handlebars from "handlebars"
import {Hono} from 'hono'

const app = new Hono()

const unsafeHTMLTemplate = Handlebars.compile("<h1>Hello {{{username}}}!</h1>")
const safeHTMLTemplate = Handlebars.compile("<h1>Hello {{username}}!</h1>")
const unsafeAttributeTemplate = Handlebars.compile(`
    <h1>Hello {{username}}!</h1>
    <img src="https://gravatar.com/avatar/{{{username}}}?d=identicon">
`)

app.get('/', (c) => c.html(unsafeHTMLTemplate({username: c.req.query("username") ?? "world"})))
app.get('/safe', (c) => c.html(safeHTMLTemplate({username: c.req.query("username") ?? "world"})))
app.get('/attr', (c) => c.html(unsafeAttributeTemplate({username: c.req.query("username") ?? "world"})))

export default app