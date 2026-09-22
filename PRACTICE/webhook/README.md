# Webhook Practice Project

## What is a Webhook?

A webhook is a way for one application to automatically send data to another application when something happens.

For example:

**Payment successful → Payment service sends webhook → Our application receives the data.**

## Why Flask?

We use **Flask** because it is a simple Python framework for creating web/API endpoints.

In this project, Flask creates our `/webhook` URL and receives the incoming HTTP request.

## Workflow

```text
External Service
      ↓
POST /webhook
      ↓
app.py
(receives request)
      ↓
webhook.py
(validates data)
      ↓
received_data.json
(saves data)
      ↓
processor.py
(processes data)
      ↓
Response
```

## How to Run

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

In another terminal, send a test webhook:

```bash
python test_webhook.py
```

The project returns an HTTP response and saves the received webhook data in `received_data.json`.


## Brief Workflow Example

**Example: Payment Successful**

```text
Customer makes payment
        ↓
Payment service detects success
        ↓
Payment service sends webhook
        ↓
Our Flask app receives the data
        ↓
Webhook is validated and processed
        ↓
Response is sent back
```

**Example data:**

```json
{
  "event": "payment_success",
  "amount": 500000,
  "customer": "Priya"
}
```
