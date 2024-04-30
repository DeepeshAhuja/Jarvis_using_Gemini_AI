import requests
from config import key, weather, mail
import socket

def get_ip(host):
    try:
        result = socket.getaddrinfo(host, None)
    except Exception as e:
        print(e)
        result = f"Error in find the IP, {e}"
    return result

def temp_room(room):
    result = f"{room} Temperature = 20, Humidity = 50"
    return result

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":city,"format":"json","u":"f"}

    response = requests.get(url, headers=weather, params=querystring)

    d1 = response.json()
    d1 = d1.get("current_observation")
    hum = d1.get("atmosphere").get("humidity")
    temp = d1.get("condition").get("temperature")
    temp = round((temp-32)*5/9,2)
    return (f"humidity:  {hum}, Temperature in C: {temp}")

def chat1(chat):
    messages = [] #list with all messages
    system_message = "You are an AI bot, your name is Jarvis. find the content related to query: " # first instruction
    message = {"role" : "user", "parts" : [{"text": system_message+" "+chat}]}
    messages.append(message)
    data = {"contents" : messages}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)
    
    t1 = response.json()
    # print(t1)
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)
    return t2

def send_email(recipient, subject, body):
    url = "https://mail-sender-api1.p.rapidapi.com/"

    your_mail_address = "deepesh.ahuja002@gmail.com"
    print(recipient,subject,body)

    payload = {
        "sendto": recipient,
        "replyTo": your_mail_address,
        "title": subject,
        "body": body
    }
    
    response = requests.post(url, json=payload, headers=mail)

    print(response.json())
    return "mail sent successfully"

definations = [
    {
        "name":"chat1",  # name of the function to be called
        "description": "find content of related query when asked normally",
        "parameters":
            {
                "type":"object",
                "properties":{
                    "chat" : {                 # Argument for function temp_city
                        "type":"string",
                        "description":"full query asked by user"
                    }
                }
            }
    },
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
    },
    {
        "name":"send_email",  # name of the function to be called
        "description": "send email using email api",
        "parameters":
            {
                "type":"object",
                "properties":{
                    "recipient" : {                 # Argument for function temp_city
                        "type":"string",
                        "description":"recipient email address"
                    },
                    "subject" : {                 # Argument for function temp_city
                        "type":"string",
                        "description":"email subject"
                    },
                    "body" : {                 # Argument for function temp_city
                        "type":"string",
                        "description":"email body content"
                    }
            }
    }
    }
]

if __name__ == "__main__":
    print(temp_city("Hyderabad"))