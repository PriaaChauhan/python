CLASSIFICATION_PROMPT = """
You are a customer support classification assistant.

Classify the customer's message into exactly one of these categories:

- billing
- refund
- technical
- other

Return only valid JSON in this format:

{{
    "category": "billing"
}}

Customer message:
{message}
"""