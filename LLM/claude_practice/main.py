

import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(
    api_key = os.environ["ANTHROPIC_API_KEY"]
)
 
try:
    message = client.messages.create(
        model="YOUR_MODEL",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": "Explain what an API is in simple words."
            }
        ]
    )

    answer = message.content[0].text
    print(answer)

except anthropic.BadRequestError as e:
    print("Request error:", e)

except Exception as e:
    print("Something went wrong:", e)