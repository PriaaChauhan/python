

# .env secret rakhta hai → Python key/read karta hai → Anthropic SDK request banane/communicate karne mein help karta hai → Claude API request Claude tak pahunchata hai → Claude answer deta hai → response wapas Python mein aata hai.

import anthropic

client = anthropic.Anthropic() # Create a client that my Python program can use to communicate with Claude


response = client.messages.create(
    model="YOUR_MODEL",
    max_tokens=500,
    messages=[
        {
            "role": "user",
            "content": "Explain what an API is in simple words."
        }
    ]

)
print(response.content[0].text)


# FLOW--------------------------------------

# .env
#  ↓
# API key
#  ↓
# Python
#  ↓
# Anthropic SDK
#  ↓
# Client
#  ↓
# Claude API
#  ↓
# Claude
#  ↓
# Response
#  ↓
# Python extracts response

