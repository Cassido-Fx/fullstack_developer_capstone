import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="https://okaforcassy-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="https://sentianalyzer.1n3cz1z5pydb.us-south.codeengine.appdomain.cloud")

# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    request_url = backend_url + endpoint
    print(f"GET from {request_url} with params {kwargs}")
    try:
        # Use the 'params' argument to pass query parameters
        response = requests.get(request_url, params=kwargs)
        return response.json()
    except requests.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None


# def analyze_review_sentiments(text):
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except requests.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {"sentiment": "neutral"}  # Default or fallback response


# def post_review(data_dict):
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        return response.json()
    except requests.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {"status": "failed"}
