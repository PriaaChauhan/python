import ollama

def ask_llm(message):
    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
            "role":"user",
            "content":message
            }
        ]
    )

    return response["message"][content]

if __name__ == "__main__":
    result = ask_llm("say hello in short sentence.")
    print(result)