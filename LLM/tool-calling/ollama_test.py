import ollama

from calculator_tool import calculate

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform basic arithmetic calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"]
                    }
                },
                "required": ["a", "b", "operation"]
            }
        }
    }
]

messages = [
    {"role": "user", "content": "What is 12 multiplied by 8?"}
]

response = ollama.chat(
    model="qwen3:4b",
    messages=messages,
    tools=tools
)

tool_call = response.message.tool_calls[0]

result = calculate(
    tool_call.function.arguments["a"],
    tool_call.function.arguments["b"],
    tool_call.function.arguments["operation"]
)
 
messages.append(response.message)

messages.append({
    "role": "tool",
    "content": str(result)
})

final_response = ollama.chat(
    model="qwen3:4b",
    messages=messages
)

print(final_response.message.content)