import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"


try:
    response = requests.get(url, timeout=10)
    data =  response.json()
    print(data)
    print(data["hourly_units"])
    print(data["hourly"]["temperature_2m"])

except Exception as e:
    print("ERROR:", e)