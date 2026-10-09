
import ollama


def ask_llm(message):
    for attempt in range(2):
        try:
            response = ollama.chat(
                model="qwen3:4b",
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as error:
            print(f"LLM attempt {attempt + 1} failed: {error}")

    print("LLM failed after 2 attempts.")
    return None