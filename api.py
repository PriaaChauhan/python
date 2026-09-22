#  we use request library in python to communicate with api and website

import requests
url =  "https://jsonplaceholder.typicode.com/posts/1"

response =  requests.get(url)
print(response.status_code)
print(response.text)

data = response.json() # --  parsing JSON to python dict so we can access response data which comes from API
# One more thing before we move on-  response.json() doesn't magically mean every response is valid JSON.
# If the server sends something that isn't valid JSON, response.json() can fail with a JSON decoding error.

 
print(data)
print(type(data)) # --  it will be dict not json


# This: response = requests.get(url) does NOT mean:
# response = the JSON data

# Instead:
# response
#    ↓
# Response object
#    ├── status code
#    ├── headers
#    ├── response body
#    └── other information

# That's why we can do things like: response.status_code, response.text


# -------------------------------------------------------------

# raise _for_status -- VERY IMPORTANT

# "If the API returned an HTTP error, raise an exception."
# That's useful because now Python is explicitly telling us:- "The HTTP request failed."



# import requests
# url = "https://jsonplaceholder.typicode.com/posts/999999"

# try:
#     response =  requests.get(url)
#     response.raise_for_status()
#     print(response.json)
# except:
#     print("The API retunred and HTTP error")