# Day 14 — Prompt Engineering

## What is Prompt Engineering?

Prompt Engineering = designing clear instructions for an LLM so it gives **accurate, consistent, and useful output**.

A good prompt tells the model:

* **What to do** → Task
* **What it needs to know** → Context
* **What rules to follow** → Constraints
* **How to respond** → Output format

---

## Core Prompt Engineering Concepts

### 1. Clearly Define the Task

Tell the LLM exactly what job it needs to perform.

Examples:

* Classify
* Extract
* Summarize
* Translate
* Generate
* Compare

### 2. Provide Useful Context

Give the information the LLM needs to perform the task correctly.

**Task ≠ Context**

* Task = What should I do?
* Context = What information should I use?

### 3. Add Constraints

Rules that control the response.

Examples:

* Use only allowed categories
* Use simple English
* Keep response short
* Don't invent information
* Handle missing information

### 4. Specify Desired Output

Tell the LLM exactly how the response should look.

Examples:

* JSON
* Bullet points
* Table
* Paragraph

**For automation, structured output (especially JSON) is very useful.**

### 5. Few-Shot Prompting

Give examples of **input → expected output** to guide the model.

* Zero-shot → No examples
* One-shot → One example
* Few-shot → Multiple examples

Useful for classification, extraction and formatting.

### 6. Role / Instruction Separation

* **System instruction** → Defines how the AI should behave.
* **User input** → Actual request/data.

Example:
`System: Extract customer information and return JSON.`
`User: Here is the customer message...`

### 7. Avoid Vague Prompts

❌ `Summarize this.`

✅ `Summarize this report in 5 short bullet points using simple English. Do not add information not present in the report.`

Clear instructions → more predictable output.

### 8. Structured Responses

Instead of free-form text, define a fixed structure.

Example:

```json
{
  "name": "...",
  "email": "...",
  "company": "..."
}
```

Useful because Python/CRM/database can process the fields automatically.

### 9. Reusable Prompts

Don't hardcode one customer's message.

Use a variable/placeholder:

```text
customer_message = {customer_message}
```

Same prompt → can process many inputs.

### 10. Improve a Bad Prompt

Typical improvement flow:

**Vague prompt → Define task → Add context → Add constraints → Define output → Test → Improve**

---

# 3 Business Prompt Patterns

## 1. Customer Support Classification

**Purpose:** Decide which category a customer message belongs to.

Example categories:

* billing
* refund
* technical
* other

**Flow:**
`Customer message → LLM → Category`

---

## 2. Lead / Customer Information Extraction

**Purpose:** Extract useful fields from customer text.

Common fields:

* name
* company
* email
* requirement

Important rule:
**If information is missing → don't guess.**

Example:

```json
{
  "name": "Rahul",
  "company": "ABC",
  "email": "not provided",
  "requirement": "AI chatbot"
}
```

**Flow:**
`Customer message → LLM → Structured data → CRM/Database`

---

## 3. Text Summarization / Business Report

**Purpose:** Convert long business text into a short, useful summary.

Common instructions:

* Keep it short
* Use simple English
* Use bullet points
* Don't miss important information
* Don't invent or assume

**Flow:**
`Long report → LLM → Short summary`

---

# Key Day 14 Takeaway

A good production-style prompt should make the LLM's job and expected output **clear and predictable**.

**Task + Context + Constraints + Output Format + Input**

And always **test the prompt with different inputs** before using it in an automation workflow.
