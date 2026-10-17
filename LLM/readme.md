# 🧠 LLM — Quick Revision

## 1. What is an LLM?

**LLM = Large Language Model**

An LLM is an AI model trained on a **huge amount of data** so it can understand and generate human-like language.

Examples:

* GPT
* Claude
* Gemini

Think:

> **LLM = AI model that is very good at working with language.**

---

## 2. Is an LLM an AI Tool?

Not exactly.

An **LLM is an AI model**.

Tools/apps such as ChatGPT or Claude use LLMs to provide an interface that people can interact with.

Simple idea:

LLM = Brain/model
ChatGPT/Claude = Application using a model

---

## 3. Where does the LLM get so much data?

Before we use an LLM, it goes through **training**.

Training data can include:

* Books
* Web content
* Articles
* Code
* Other datasets
* Human-written text

Very simplified:

Huge amount of data
        ↓
     Training
        ↓
Model learns patterns
        ↓
    Trained LLM
 

## 4. Does the LLM simply store all the data?

❌ Not like a normal database.

During training, the model's **parameters/weights are adjusted** so it learns patterns in the data.

For example, after seeing many examples of language, it learns patterns about:

* words
* grammar
* relationships between concepts
* how sentences are formed
* how different types of text are written

So:

> **LLM ≠ giant database**

It is a trained mathematical model that has learned patterns from data.

---

## 5. How does an LLM answer?

You give it an input/prompt:

```text
"Explain APIs in simple language."
```

The trained model processes the input and generates an answer based on the patterns it learned.

```text
Your prompt
     ↓
  Trained LLM
     ↓
Generated response
```

---

## 6. LLM vs Traditional Software

### Traditional software

A developer writes explicit rules:

```text
Input
 ↓
Programmed rules
 ↓
Output
```

Example:

```text
10 + 5
  ↓
Addition logic
  ↓
15
```

### LLM

```text
Input + instructions
        ↓
      LLM
        ↓
Generated output
```

Example:

```text
"Explain this angry customer email."
        ↓
      LLM
        ↓
"Customer is frustrated because..."
```

### Main difference

> **Traditional software follows explicitly programmed rules.**

> **LLMs generate outputs using patterns learned during training.**

---

## 7. Training vs Using an LLM

### Training

The model learns from huge amounts of data.

```text
Data → Training → Model
```

### Using

You use an already-trained model.

```text
Your prompt → Trained LLM → Response
```

You are normally **using** an LLM when you chat with ChatGPT or Claude; you are not training the model from scratch.

---

## 8. Does the LLM know my company's data?

❌ Not automatically.

Suppose a company has:

```text
Customer database
Internal documents
Orders
Private emails
Company policies
```

The LLM does not automatically know this private information.

An AI automation can give the model access to relevant information through:

* APIs
* Databases
* Files
* RAG
* Tools

So remember:

```text
Training data
     ↓
General knowledge/patterns

Company data
     ↓
Specific information provided to the AI system
```

---

# ⭐ Most Important Mental Model

```text
             LLM
              │
     ┌────────┴────────┐
     ↓                 ↓
 Learned patterns   Generates language
 from training      from your input
     │
     ↓
Books / web / code /
datasets / text
```

And in **AI Automation**:

```text
User
 ↓
LLM → Understand / generate language
 ↓
Python → Logic
 ↓
API → Perform an action
 ↓
Database / Service
 ↓
LLM → Create response
 ↓
User
```

## 🧠 One-line revision

> **An LLM is a trained AI model that learns patterns from huge amounts of data and uses those learned patterns to understand and generate language.**


# LLM Core Concepts 🧠

## 1. Tokens

**Token = small piece of text that an LLM processes.**

```text
"I love Python!"
       ↓
Tokenizer
       ↓
"I" | " love" | " Python" | "!"
```

* Token ≠ always one word.
* User prompt → **input tokens**
* LLM response → **output tokens**

---

## 2. Context Window

**Context window = maximum amount of tokens the model can handle in one interaction.**

```text
Prompt
+ Previous relevant chat
+ Instructions
+ Other information
        ↓
   CONTEXT WINDOW
        ↓
       LLM
        ↓
   Output tokens
```

* Model provider decides the maximum context size.
* Longer prompt/conversation = more tokens used.
* Context window ≠ permanent memory.

---

## 3. Parameters / Weights

**Parameters = numerical values inside the model that are adjusted during training.**

```text
Training data
     ↓
Training
     ↓
Parameters / Weights
     ↓
Trained LLM
```

* The **model provider/developer trains the model**.
* Parameters contain the patterns learned during training.
* `7B parameters` = approximately **7 billion parameters**.

---

# 🔥 Remember

```text
TRAINING
Data → Training → Parameters → Trained LLM

USING
Prompt → Tokens → Context Window → LLM → Output Tokens
```

### One-line difference:

**Tokens** = pieces of text
**Context Window** = maximum token capacity for the context
**Parameters** = learned numerical values inside the trained model

Parameter count tells you about model size, not a universal quality ranking.



## 1. Temperature

* **Temperature** controls how predictable or varied the LLM's response is.
* **Low temperature** → more consistent/predictable output.
* **High temperature** → more varied/creative output.
* Low temperature is useful for structured tasks; higher temperature can be useful for creative tasks.
* **Temperature ≠ intelligence.**

---

## 2. Hallucinations

* **Hallucination** = when an LLM gives false, made-up, or unsupported information.
* An LLM generates responses based on learned patterns; it is not automatically a fact-checker.
* Example: AI confidently giving an incorrect fact.
* In automation, important outputs should be **validated** instead of blindly trusted.

---

## 3. Token Usage

* **Token usage** = the amount of text processed by the LLM in tokens.
* **Input tokens** → tokens in your prompt/input.
* **Output tokens** → tokens in the AI response.
* **Total token usage ≈ Input tokens + Output tokens.**
* More tokens generally mean **more usage, potentially more cost, and more processing time.**

---

## 4. Latency

* **Latency** = how long it takes to receive the LLM response.
* Example: You send a prompt → response arrives after 2 seconds → latency is about 2 seconds.
* Longer/complex requests and different models can affect latency.
* In AI automation, lower latency generally means a **faster user experience**.

---

### Quick Memory

**Temperature** → How varied is the response?
**Hallucination** → Can the AI make things up?
**Token usage** → How much text is processed?
**Latency** → How long do I wait?


# Claude API

## 1. What is an LLM API?

An **LLM API** allows a Python/application to communicate with an LLM.

Python → LLM API → LLM → Response → Python


Example: Python sends a question to Claude and receives Claude's answer.

---

## 2. Claude vs Claude API

* **Claude** = LLM/model made by Anthropic.
* **Claude API** = interface that allows applications to communicate with Claude.
* **Claude App** = human uses Claude directly.
* **Claude API** = program uses Claude.

---

## 3. Anthropic SDK

**SDK (Software Development Kit)** = Python library that makes working with Claude API easier.

Without the SDK, we would have to manually build HTTP requests.

---

## 4. Claude Client

client = anthropic.Anthropic(...)

`client` is the Python object used to communicate with the Claude API.

Think:

```text
Anthropic SDK = toolbox
client = tool used to communicate with Claude
```

---

## 5. API Key

API key is used to **authenticate** our application.

Never hardcode it:

api_key = "MY_SECRET_KEY"   # ❌

Use an environment variable:

```text
ANTHROPIC_API_KEY=your_key
```

And keep `.env` out of GitHub:

```text
.env
venv/
```

inside `.gitignore`.

---

## 6. Loading `.env`

`python-dotenv` loads variables from `.env`.

```python
from dotenv import load_dotenv

load_dotenv()
```

Then Python can access:

```python
os.environ["ANTHROPIC_API_KEY"]
```

---

## 7. Basic Claude API Request

```python
message = client.messages.create(
    model="...",
    max_tokens=500,
    messages=[
        {
            "role": "user",
            "content": "Explain API in simple words."
        }
    ]
)
```

Main parts:

* `model` → which Claude model should process the request
* `max_tokens` → maximum amount of response tokens allowed
* `messages` → conversation/input

---

## 8. Messages

Anthropic Messages API uses:

```python
messages=[
    {
        "role": "user",
        "content": "Your question here"
    }
]
```

### `role`

Tells who is sending the message.

```text
user → user's input
```

### `content`

The actual instruction/question.

---

## 9. System Instruction

System instruction tells Claude **how it should behave / what role it should follow**.

Example:

```python
system="You are an email classifier. Return only SPAM or NOT_SPAM."
```

Think:

```text
System = overall rules/behavior
User = actual task
```

---

## 10. User Instruction

The user instruction is the actual work Claude needs to perform.

Example:

```text
System:
You are an email classifier.

User:
Classify this email: "You won $10,000!"
```

---

## 11. Model Selection

`model` tells Claude API which model should handle the request.

Model choice depends on:

* Task complexity
* Capability
* Speed/latency
* Cost
* Context limits

Don't blindly memorize model names because available models can change.

---

## 12. Request → Response Flow

```text
Python
  ↓
Anthropic SDK
  ↓
Claude API
  ↓
Claude Model
  ↓
Response
  ↓
Python
```

---

## 13. Important Response Concept

Claude doesn't simply return a normal Python string.

The API returns a **structured response object**.

To extract generated text:

```python
print(message.content[0].text)
```

Meaning:

```text
message
  ↓
content
  ↓
first content block [0]
  ↓
text
```

We still need to practice response parsing properly.

---

## 14. API Errors

API calls can fail.

Example we encountered:

```text
anthropic.BadRequestError
```

Our actual error was:

```text
Your credit balance is too low
```

Important lesson:

**API error ≠ Python code error necessarily.**

Errors can happen because of:

* Invalid API key
* No credits
* Invalid request
* Wrong model
* Rate limit
* Network/API problems

Proper `try/except` error handling is still remaining to practice.

---

## 15. Claude Pro vs Claude API

They are separate.

```text
Claude Pro
   ↓
Claude app / supported Claude features

Claude API
   ↓
Python applications / automation
```

A Claude Pro subscription does **not automatically provide normal API credits**.

For now, we are learning the API without spending money.

---

## 16. Real AI Automation Example

Example: Email classifier

```text
Incoming Email
      ↓
Python
      ↓
Claude API
      ↓
Claude
      ↓
SPAM / NOT_SPAM
      ↓
Python
      ↓
Take action
```

This is the type of API → Python → AI → automation workflow used in real applications.

---

# Day 12 Key Takeaway

The main thing to understand:

> **Claude API allows our Python application to send instructions to Claude and receive an AI-generated response that our program can then use.**

Basic structure:

```python
client.messages.create(
    model="...",
    max_tokens=500,
    system="...",
    messages=[
        {
            "role": "user",
            "content": "Your task"
        }
    ]
)
```

### Still Remaining

* [ ] Properly parse Claude response
* [ ] Handle API errors with `try/except`
* [ ] Complete small Python Claude script
* [ ] Test different prompts
* [ ] Clean project + README
* [ ] Push working code