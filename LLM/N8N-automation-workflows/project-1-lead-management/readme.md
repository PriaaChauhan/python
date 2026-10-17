# Lead Management Automation

## Overview

Lead Management Automation is an n8n workflow that receives new lead information through a webhook, cleans the incoming data, checks whether the lead's email already exists in Google Sheets, and routes the request based on whether the lead is new or a duplicate.

## Problem Statement

Manually recording leads and checking for duplicate entries can waste time and lead to inconsistent records. This workflow automates lead intake and duplicate checking.

## Workflow

1. **Webhook:** Receives incoming lead data through an HTTP POST request.
2. **Edit Fields:** Extracts and organizes lead information such as name, email, company, requirement, source, and status.
3. **Google Sheets — Get Row(s):** Searches for an existing lead using the email address.
4. **IF:** Determines whether a matching lead already exists.
5. **Duplicate response:** Returns a response indicating that the lead already exists.
6. **Google Sheets — Append Row:** Adds a new lead when no matching email is found.
7. **Respond to Webhook:** Returns the relevant result to the caller.

## Example Input

```json
{
  "name": "Aarav Sharma",
  "email": "aarav@example.com",
  "company": "ABC Technologies",
  "requirement": "AI customer support automation",
  "source": "website",
  "status": "new"
}
```

The exact request structure depends on the webhook configuration.

## Technologies Used

- n8n
- Webhooks and HTTP POST
- Google Sheets
- IF conditions
- JSON
- Postman

## Key Features

- Automated lead intake
- Email-based duplicate checking
- Conditional workflow routing
- Automated Google Sheets data entry
- HTTP response handling

## Testing

Test with a new email address and then submit the same email again. Verify that the first request creates a record and the duplicate request follows the duplicate-handling path.

## Limitations and Future Improvements

- Add input validation and more detailed error handling.
- Add CRM integration.
- Introduce AI-based lead qualification and prioritization.

## Project Files

- `workflow.json` — exported n8n workflow.
- `README.md` — project documentation.

## Security Note

This workflow may depend on separately configured n8n credentials and a Google Sheets connection. Configure your own credentials after importing it. Never publish API keys, access tokens, private webhook URLs, or real customer information.