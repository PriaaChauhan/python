# This file contains the actual processing of our webhook data.
# webhook.py will send the data here.

def process_webhook(data):

    # Get the event name from the received data
    event = data.get("event")

    # Check what type of event we received
    if event == "payment_success":
        print("Payment was successful!")

    else:
        print("Unknown event received")

    # Return a result after processing
    return {"message": "Data processed successfully"}