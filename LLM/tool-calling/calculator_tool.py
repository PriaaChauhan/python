def calculate(a,b,operation):
    if operation == "add":
        return(a+b)
    elif operation == "multiply":
        return(a*b)
    elif operation == "subtract":
        return(a-b)
    elif operation == "divide":
        return(a/b)
    else:
        return("invalid operation")

# print(calculate(2,3, "add"))
# print(calculate(2,3, "subtract"))
# print(calculate(2,3, "multiply"))
# print(calculate(2,3, "divide"))
# print(calculate(2,3, "dive"))  #invalid


#SCHEMA 

schema = {
    "tool_name": "calculator",
    "description": "Perform basic arithmetic calculations",
    "parameters": {
        "a": "number",
        "b": "number",
        "operation": "string"
    },
    "allowed_operations": ["add", "multiply", "divide", "subtract"]
}
