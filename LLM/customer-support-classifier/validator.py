import json 

ALLOWED_CATEGORIES = {
    "billing",
    "refund",
    "technical",
    "other"
}
def parse_json(response):
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return None


def validate_category(data):
    if not isinstance(data,dict): #isinstance() is a Python built-in function used to check:
         # "Is this value of this particular data type?"
        return False
    if "category" not in data: #1. Does the field exist?
        return False
    if data["category"] not in ALLOWED_CATEGORIES: #2. If it exists, is its value allowed?
        return False
    return True 


