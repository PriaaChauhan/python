# OpenAI API — Day 13

## Basic Flow

Python App
↓
OpenAI SDK
↓
OpenAI API
↓
GPT Model
↓
Response
↓
Python App

## Key Concepts

* **OpenAI** → LLM provider/company
* **GPT** → OpenAI's model family
* **OpenAI SDK** → Python library used to communicate with OpenAI API
* **Client** → Interface between our Python app and OpenAI API
* **API key** → Used to authenticate API requests

## API Key

Store the key in an environment variable:

`OPENAI_API_KEY`

The OpenAI SDK can automatically read this environment variable, so we don't have to manually pass the key every time.

## Basic Python Pattern

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="...",
    input="Your prompt"
)

print(response.output_text)
```

### What happens?

* `OpenAI()` → creates the API client
* `responses.create()` → sends the request to the model
* `model` → selects which model to use
* `input` → sends the prompt/task
* `response.output_text` → gets the generated text

## Important

OpenAI, Claude and Gemini may use different SDKs and syntax, but the **basic API pattern is the same**:

**Python → SDK → Provider API → Model → Response**
