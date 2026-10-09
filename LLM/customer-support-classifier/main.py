from prompts import CLASSIFICATION_PROMPT 
from llm import ask_llm
from validator import parse_json, validate_category
from storage import save_result

customer_message = input("Enter customer message: ")
if not customer_message.strip():
    print("Error: Customer message cannot be empty.")
    exit()

prompt = CLASSIFICATION_PROMPT.format(message = customer_message)
result = ask_llm(prompt)

if result is None:
    print("Error: Could not get a response from the LLM")
    exit()

data = parse_json(result)

if data is None:
    print("Error: LLM returned invalid JSON")

elif validate_category(data):
    data["message"] = customer_message

    save_result(data)

    print("Valid classification:", data)
    print("Result saved successfully!")

else:
    print("Error: Invalid category or response structure")