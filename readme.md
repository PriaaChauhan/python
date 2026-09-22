mutable  data types - dictionary , lists, sets

immutable data types(cannot be change in same place stored in memory) - string, int, tuples, float, boolean, complex


REGISTERS -- FLIP FLOP -  LOGIC GATES - DIODES

One sentence to remember:

🖨️ print() = "Show this to me."
📦 return = "Give this back to me so I can use it."

-------------------------------------------------------------

# API
 -  a way for one program communicate with other programs.
Then what is REST?
--- REST is a commonly used way of designing APIs around HTTP.
A REST API is an API that commonly uses HTTP methods and URLs to work with resources/data.-
For example, imagine a contact API:

GET    /contacts
POST   /contacts
GET    /contacts/5
PATCH  /contacts/5
DELETE /contacts/5

Notice what we're doing?

We're using the HTTP methods you just learned:

GET     → read
POST    → create
PATCH   → partially update
DELETE  → delete

That's the connection.

# URL = the web address

# Endpoint = a specific API address you interact with
--------------------------------------------------------------

# PARAMETERS-

1. Path parameter 
what if we want contact #5?
We could have:
/contacts/5

Here:
/contacts/5
         ↑
    path parameter
The 5 identifies the specific contact.


2. query parameter
Now imagine you don't want one specific contact.You want to search contacts.

You might have:
/contacts?name=priya

Here:
?name=priya is a query parameter.
The ? basically starts the query parameters


# reuqest body 
Request body = data you're sending to the server.

# response body
The server processes your request and sends something back.

 # API key

If someone asks:

"What is an API key?"
Your simple answer should be:

An API key is a credential provided by an API service that a program sends with its requests so the service can identify/control access to that client or application.


# BEARER TOKEN   
A Bearer token is a credential that your program sends to an API to prove it has access.
The word "Bearer" basically means: Whoever bears (possesses) this token can use it.

#  API vs Bearer token
API key:
"Here is my API key. I have access to this API."

Bearer token:
"Here is my access token. I'm presenting this token to access the API."
And one important point: the exact behavior isn't universal. Some APIs use API keys for authentication, some use bearer tokens, and OAuth commonly results in bearer access tokens.


# OAuth
OAuth allows an application to get limited access to another service on behalf of a user without requiring the user's password.


 Your app
   ↓
User logs in / gives permission
   ↓
OAuth authorization
   ↓
Access token
   ↓
Your app
   ↓
Authorization: Bearer XYZ789
   ↓
API

# api vs bearer vs oauth
API key → a type of credential.
Token → a broad term for a credential.
Bearer → a way of presenting a token: "whoever possesses this token can present it."
OAuth → a protocol/framework that can be used to obtain delegated access tokens.
🧠 One-line memory trick

API key = credential, Token = general credential term, Bearer = how a token is presented, OAuth = the authorization process that can give you the token.


## Webhook vs API

**API:** Our application asks another service for data.

**Webhook:** Another service automatically sends data to our application when an event happens.

**Easy way to remember:**

* API → **"Give me the data."**
* Webhook → **"I'll tell you when something happens."**
