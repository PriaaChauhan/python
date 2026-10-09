# Day 19 — Customer Support Classifier

## Project Overview

A beginner-friendly LLM application that classifies customer support messages into categories using a local LLM (Ollama + Qwen3:4b).

**Goal:** Understand how to build an end-to-end LLM application without paying for API credits.

## Application Flow

Customer Message → Input Validation → Prompt Creation → LLM Classification → JSON Parsing → Output Validation → Save to JSON File

## Project Structure

* `main.py` — Runs the complete application.
* `llm.py` — Sends prompts to the local Ollama model and handles retries.
* `prompts.py` — Contains the classification prompt.
* `validator.py` — Parses JSON and validates the response.
* `storage.py` — Saves valid results to a JSON file.
* `data/results.json` — Stores classified customer messages.
* `tests/test_cases.py` — Tests JSON parsing and validation.
* `requirements.txt` — Lists Python dependencies.
* `.gitignore` — Prevents virtual environments, cache files, and secrets from being tracked.
* `.env` — Reserved for environment variables; no API key is required for this local Ollama setup.

## Supported Categories

* `billing` — Payment or billing problems.
* `refund` — Refund requests.
* `technical` — Technical issues.
* `other` — Messages that don't fit the other categories.

## How to Run

1. Start Ollama and ensure the `qwen3:4b` model is available.

2. Activate your Python virtual environment.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python3 main.py
   ```

5. Enter a customer message and check the classification and saved results.

## Error Handling

* Rejects empty customer messages.
* Retries failed LLM requests.
* Handles invalid JSON responses.
* Validates required fields and allowed categories.
* Prevents invalid classifications from being saved.

## Testing

Run from the project folder:

```bash
python3 tests/test_cases.py
```

The tests cover valid categories, missing categories, invalid categories, invalid JSON, and non-dictionary JSON responses.

## Key Learnings

* Building an end-to-end LLM application.
* Writing effective prompts.
* Using a local LLM without paid API credits.
* Parsing and validating structured JSON.
* Handling errors and retrying failed requests.
* Saving results to a JSON file.
* Writing basic automated tests.
* Organizing Python code into separate modules.

## Interview Explanation

"I built a customer support classification application using Python and a locally running LLM. It accepts a customer message, classifies it into a predefined category, validates the JSON response, and saves valid results. I also implemented basic error handling, retries, and automated tests."

## Future Improvements

* Add more test cases and improve failure handling.
* Store results in a database.
* Integrate the classifier with a CRM or support ticket system.
* Add a web API using Flask or FastAPI.
