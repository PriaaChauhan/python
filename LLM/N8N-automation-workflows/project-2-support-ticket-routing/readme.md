# Customer Support Ticket Routing Automation

## Overview

Customer Support Ticket Routing Automation is an n8n workflow that receives support tickets through a webhook, organizes the incoming data, routes tickets according to their category, and handles high-priority tickets differently from normal-priority tickets.

## Problem Statement

Support teams often receive tickets involving billing, technical issues, and account-related queries. Manually routing tickets can delay responses, particularly for urgent requests.

This workflow demonstrates how rule-based automation can route tickets and return structured responses.

## Workflow

1. **Webhook:** Receives a support ticket through an HTTP POST request.
2. **Edit Fields:** Extracts ticket ID, customer email, message, category, and priority.
3. **Switch:** Routes the ticket according to its supplied category:
   - `billing`
   - `technical`
   - `account`
4. **IF:** Checks whether the ticket priority equals `high`.
5. **High-priority response:** Returns an escalation-related response when the condition is true.
6. **Normal-priority response:** Returns the normal routing response when the condition is false.
7. **Fallback output:** Handles categories that do not match the configured Switch rules.
8. **Respond to Webhook:** Returns a JSON response to the caller.

## Example Input

```json
{
  "ticketId": "T-1001",
  "customerEmail": "customer@example.com",
  "message": "I was charged twice for my subscription",
  "category": "billing",
  "priority": "high"
}
```

## Technologies Used

- n8n
- Webhooks and HTTP POST
- Switch routing
- IF conditions
- JSON
- Postman

## Key Features

- Automated ticket intake
- Category-based routing
- High-priority and normal-priority handling
- Fallback handling for unknown categories
- Structured HTTP responses

## Testing

Seven scenarios were tested:

- Billing with high priority
- Billing with normal priority
- Technical with high priority
- Technical with normal priority
- Account with high priority
- Account with normal priority
- Unknown category

## Limitations and Future Improvements

- Categories and priorities are supplied by the incoming request; the workflow does not currently infer them from free-text messages.
- Add validation for invalid priority values.
- Integrate OpenAI for AI-based category classification, priority assessment, and ticket summarization.
- Integrate a CRM or ticketing platform for persistent ticket management.

## Project Files

- `workflow.json` — exported n8n workflow.
- `README.md` — project documentation.

## Security Note

Configure your own n8n credentials and webhook settings after importing. Do not publish API keys, private webhook URLs, customer data, or other sensitive information.