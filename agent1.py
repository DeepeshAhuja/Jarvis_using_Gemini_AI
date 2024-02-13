# this file execute the respective function based on user query
import task1
import requests
from config import key

# response to function call
# {'candidates': [{'content': {'parts': [{'functionCall': {'name': 'temp_city', 'args': {'city': 'Hyderabad'}}}], 'role': 'model'},
# response to hi
# {'candidates': [{'content': {'parts': [{'text': 'I am an AI bot that can do tasks using function calls. I am here to help you. Let me know what you need assistance with and I will provide responses using function calls.'}], 'role': 'model'}, 

def parse_function_response(message):
    function_call = message[0].get("functionCall") #[{'functionCall': {'name': 'temp_city', 'args': {'city': 'Hyderabad'}}}]
    function_name = function_call.get("name") #{'name': 'temp_city', 'args': {'city': 'Hyderabad'}}
    print("Gemini: function call",function_name)
    try:
        arguments=function_call.get("args","Hyderabad")
        print("Gemini: arguments are",arguments)
        if arguments:
            d=getattr(task1,function_name)
            print("function is",d)
            function_response = d(**arguments)
        else:
            function_response = "No arguments are present"
    except Exception as e:
        print("Error: ",e)
        function_response = "Invalid response"
    return function_response

def run_conversation(user_message):
    messages = [] #list with all messages
    
    system_message = """You are an AI bot that can do everything using function call. 
                      when you are asked to do something use the function call you have available 
                      and then respond with message """ # first instruction
    message = { "role" : "user", 
                "parts" : [{"text": system_message+"\n"+user_message}]}
    
    messages.append(message)
    
    data = {"contents" : [messages],
            "tools":
                [{
                    "functionDeclarations" : task1.definations
                }]
            }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)
    
    if response.status_code != 200:
        print(response.text)
    
    t1 = response.json()
    if "content" not in t1.get("candidates")[0]:
        print("Error: No content in response")
        
    message = t1.get("candidates")[0].get("content").get("parts")
    if 'functionCall' in message[0]:
        resp1 = parse_function_response(message)
        return resp1
    
    print("now we are getting",t1)
    # t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    # print(t2)
    
if __name__ == "__main__":
    user_message = "find ip address of google.com"
    print(run_conversation(user_message))