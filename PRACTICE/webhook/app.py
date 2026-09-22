

# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/webhook", methods=["POST"]) # we created one webhook url endpoint, now whenever any external service hit this URL , this function call ->
# def receive_webhook():
#     data = request.json  # Get the JSON data sent by the external service
#     print(data)

#     return {"message": "Webhook received"}, 200 # Send a response back to the sender(external service)

# if __name__ == "__main__":
#         app.run(debug = True)


# we wont call receive_webook() function manually as we do in pyhton , instead -  FLAST WILL DO THIS AUTIMATICALLY WHEN CORRECT REQUEST HIT WEBHOOK URL

from flask import Flask, request
from webhook import handle_webhook

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def receive_webhook():

    # Get the JSON data sent by the external service
    data = request.json

    # Send the received data to webhook.py
    result, status_code = handle_webhook(data)

    return result, status_code
    # Send the result back to the external service
    


if __name__ == "__main__":
    app.run(debug=True)