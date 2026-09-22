import json

from processor import process_webhook


def handle_webhook(data):

    # Check whether any data was received
    if not data:
        return {"message": "No data received"}, 400

    # These fields are required for our payment webhook
    required_fields = ["event", "amount", "customer"]

    for field in required_fields:

        # If a required field is missing, reject the webhook
        if field not in data:
            return {"message": f"{field} is missing"}, 400

    # Try to save the webhook data
    try:

        # Open the JSON file in write mode
        with open("received_data.json", "w") as file:

            # Convert Python dictionary into JSON and save it
            json.dump(data, file, indent=4)

    # If something goes wrong while saving the file
    except Exception as error:

        # Print the actual error so we can understand what happened
        print("Error saving webhook data:", error)

        # Tell the sender that our server had a problem
        return {"message": "Could not save webhook data"}, 500

    # If saving worked, send the data to processor.py
    result = process_webhook(data)

    # Return the processing result
    return result, 200