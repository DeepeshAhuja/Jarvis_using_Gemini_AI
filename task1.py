import requests
from config import headers
import socket

def get_ip(host):
    try:
        result = socket.getaddrinfo("google.com", None)
    except Exception as e:
        print(e)
        result = f"Error in find the IP, {e}"
    return result

def temp_room(room):
    result = "Temperature = 20, Humidity = 50"
    return result

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":city,"format":"json","u":"f"}

    response = requests.get(url, headers=headers, params=querystring)

    d1 = response.json()
    d1 = d1.get("current_observation")
    hum = d1.get("atmosphere").get("humidity")
    temp = d1.get("condition").get("temperature")
    temp = round((temp-32)*5/9,2)
    return (f"humidity:  {hum}, Temperature: {temp}")

definations = [
    {
        "name":"temp_city",  # name of the function to be called
        "description": "find weather, temperature of a city",
        "parameters":
            {
                "type":"object",
                "properties":{
                    "city" : {                 # Argument for function temp_city
                        "type":"string",
                        "description":"city to find weather"
                    }
                }
            }
    },
    {
        "name":"temp_room",  # name of the function to be called
        "description": "find temperature of my room or my home",
        "parameters":
            {
                "type":"object",
                "properties":{
                    "room" : {                 # Argument for function temp_city
                        "type":"string",
                        "description":"room or home"
                    }
                }
            }
    },
    {
        "name":"get_ip",  # name of the function to be called
        "description": "find ip address of given url or domain name",
        "parameters":
            {
                "type":"object",
                "properties":{
                    "host" : {                 # Argument for function temp_city
                        "type":"string",
                        "description":"get url or domain name"
                    }
                }
            }
    }
]

if __name__ == "__main__":
    print(temp_city("Hyderabad"))