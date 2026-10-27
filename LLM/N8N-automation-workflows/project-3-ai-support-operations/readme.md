# AI Support Operations Automation with RAG and Human Approval

## Overview

AI Support Operations is an n8n automation project that processes incoming customer support tickets, classifies them using an AI model, retrieves relevant support knowledge using Retrieval-Augmented Generation (RAG), routes tickets, and stores ticket information in a data table.

A separate approval API allows an authorized reviewer to approve or reject tickets that are awaiting human review.

The project demonstrates how AI, workflow automation, vector search, API integration, data persistence, and human-in-the-loop controls can work together in a support operations workflow.

## Problem Statement

Support teams receive tickets involving billing problems, account access, and technical issues. Manually reviewing, classifying, routing, and tracking every ticket can take time and lead to inconsistent handling.

AI can help classify and summarize incoming tickets, while a knowledge base can provide relevant support information. However, sensitive or important decisions may still require human review.

This project automates the ticket-processing workflow while keeping approval decisions separate and preventing repeated decisions from changing an already processed ticket.

## Project Architecture

### Main Workflow — AI Support Operations

1. **Webhook:** Receives a support ticket through an HTTP POST request.
2. **Input Validation and Normalization:** Checks required fields and normalizes ticket information, including the customer email.
3. **Knowledge Retrieval (RAG):** Retrieves relevant support knowledge from a Qdrant vector database.
4. **AI Classification:** Uses an AI model to classify the ticket and produce structured fields such as category, priority, sentiment, and summary.
5. **Ticket Routing:** Routes the ticket according to its classification and handling rules.
6. **Duplicate Detection:** Checks whether the ticket ID already exists in the ticket data table.
7. **Data Persistence:** Saves a new ticket and its processing or approval information when appropriate.
8. **Webhook Response:** Returns a structured JSON response to the caller.

### Approval Workflow — AI Support Ticket Approval API

1. **Approval Webhook:** Receives a ticket ID, an approval action, the reviewer's name, and a note.
2. **Request Validation:** Checks that the required fields are present and the action is valid.
3. **Ticket Lookup:** Searches the ticket data table for the requested ticket.
4. **Approval Eligibility Check:** Verifies that the ticket exists and is still awaiting approval.
5. **Data Table Update:** Updates the existing ticket with the approval decision and related review information.
6. **Response Handling:** Returns the appropriate result for valid decisions, missing tickets, invalid requests, or tickets that have already been processed.

Repeated approval or rejection requests do not reprocess a ticket that is no longer pending approval.

## Retrieval-Augmented Generation (RAG)

The project uses a support knowledge base containing troubleshooting and support-handling information.

Example knowledge-base topics include:

- Password reset troubleshooting
- Duplicate subscription charges
- Locked account handling

The knowledge documents are embedded and stored in Qdrant so that relevant information can be retrieved for incoming support requests.

The knowledge base includes handling rules such as not asking customers to share passwords or verification codes, and not promising a refund before it has been confirmed.

RAG provides relevant knowledge to the AI workflow; retrieval quality depends on the documents, embeddings, and search configuration.

## Example Input — Main Workflow

Send an HTTP POST request with a JSON body such as:

```json
{
  "ticketId": "TKT-DEMO-001",
  "customerEmail": "customer@example.com",
  "message": "I was charged twice for my subscription."
}
```

The AI workflow processes the ticket and generates structured classification information. The exact classification and routing result depends on the model output and configured workflow rules.

## Example Input — Approval API

To approve a ticket that is awaiting approval:

```json
{
  "ticketId": "TKT-DEMO-001",
  "action": "approve",
  "approvedBy": "Demo Reviewer",
  "note": "Reviewed and approved."
}
```

To reject a pending ticket, use `"action": "reject"` and provide an appropriate review note.

The ticket must already exist and be in the pending-approval state for the decision to be applied.

## Technologies Used

- n8n Cloud
- AI model and structured output
- Retrieval-Augmented Generation (RAG)
- Qdrant Vector Database
- Embeddings and vector similarity search
- Webhooks and REST API
- JSON
- n8n Data Tables
- Postman
- Google Drive knowledge documents

## Key Features

- Automated ticket intake and input validation
- AI-based ticket classification and summarization
- Category and priority-based routing
- Retrieval of relevant support knowledge
- Duplicate ticket ID detection
- Persistent ticket storage
- Separate approval and rejection API
- Validation of approval requests
- Protection against repeated decisions on already processed tickets
- Structured webhook responses

## Setup and Testing

### Prerequisites

- An n8n instance
- Access to an AI model compatible with the imported workflow
- A Qdrant collection configured for the required embedding dimensions
- The required support knowledge documents
- An n8n Data Table named `support_tickets_v2`, with the fields expected by the workflows
- Postman or another HTTP client

### Import the Workflows

1. Download `workflow.json` and `approval-workflow.json` from this repository.
2. Open your n8n instance.
3. Import each JSON file as a separate workflow.
4. Reconnect the required credentials using your own accounts.
5. Configure the Qdrant collection, embedding model, knowledge documents, and Data Table as required.
6. Review the webhook paths and node configurations.
7. Test the workflows using their test webhook URLs before enabling production execution.

Imported workflows may require configuration adjustments depending on the n8n version and available credentials.

### Test the Main Workflow

1. Start a test execution and send the example ticket payload to the main workflow's test webhook URL.
2. Inspect the execution to verify validation, knowledge retrieval, AI classification, and routing.
3. Confirm that the ticket is saved to the data table.
4. Submit the same ticket ID again and verify the duplicate-handling branch.
5. Inspect the webhook response and relevant node outputs.

### Test the Approval Workflow

Use the approval webhook's test URL and send requests through Postman.

Test these scenarios:

- Approve a pending ticket.
- Reject a pending ticket.
- Submit another decision for an already processed ticket.
- Submit an unknown ticket ID.
- Submit an invalid action or omit a required field.

Verify the HTTP response, execution path, and data table state for each scenario. An already processed ticket should not be updated by a repeated decision.

## Security Notes

- Do not commit API keys, passwords, access tokens, or private credentials.
- Use your own credentials when importing the workflows.
- Do not publish private webhook URLs or real customer information.
- Use demo payloads and anonymized data in public documentation.
- Protect production webhook endpoints from unauthorized requests.
- Configure appropriate access controls before exposing approval actions.

## Limitations and Future Improvements

- AI classification and retrieval quality depend on the model, prompts, embeddings, and knowledge documents.
- The current project uses n8n Data Tables rather than a dedicated production ticketing platform.
- Production deployment would require stronger authentication, authorization, monitoring, and error-handling policies.
- RAG should be evaluated using a broader set of representative questions and expected answers.
- Future improvements could include automated evaluation of retrieval quality, audit reporting, notifications, and integration with a CRM or ticketing system.

## Project Files

- `workflow.json` — exported main AI Support Operations workflow.
- `approval-workflow.json` — exported human approval API workflow.
- `README.md` — project overview, architecture, setup, and testing instructions.

## Project Status

The core workflows and approval scenarios have been tested. This repository is intended as a portfolio and learning project; additional security hardening, evaluation, and deployment work may be required before production use.