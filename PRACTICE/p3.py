# “I’m building a console-based Contact Management System in Python. It allows users to add contacts, validates phone-number input, and stores/loads contact data using JSON.”

import json

contacts = []

def addData():
    try:
        name = input("Enter your name: ")
        number = int(input("Enter your number: "))

        print("Number converted successfully")

        contact = {
            "name": name,
            "number": number
        }

        contacts.append(contact)

        print("Contact added!")

    except Exception as e:
        print("ERROR:", e)


def saveData():
    with open("practice.json", "w") as file:
        json.dump(contacts, file)


def loadData():
    try:
        with open("practice.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


contacts = loadData()
addData()
saveData()