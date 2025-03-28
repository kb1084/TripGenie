import os
import requests
import time
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_NAME = "google/gemma-2-2b-it"  # Updated model
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Debugging: Check if API key is loaded
print(f"🔍 API Key Loaded: {API_KEY is not None}")

def query_huggingface(prompt, max_retries=5):
    """Query Hugging Face API with retry logic."""
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 500,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            print(f"🔍 API Response Code: {response.status_code}")  # Debugging

            if response.status_code == 200:
                json_response = response.json()
                print(f"🔍 Full API Response: {json_response}")  # Debugging

                if isinstance(json_response, list) and len(json_response) > 0:
                    return json_response[0].get("generated_text", "⚠️ No text generated.")
                else:
                    print("⚠️ Unexpected response format, trying again...")
            elif response.status_code in [401, 404, 503]:
                print(f"❌ API Error {response.status_code}: {response.text}")
                return None
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Request error: {e}")
            return None
        
        wait_time = min(2 ** attempt, 60)  # Exponential backoff with a max wait time of 60s
        print(f"⚠️ Retrying in {wait_time} seconds...")
        time.sleep(wait_time)

    print("❌ API is still unavailable after multiple retries.")
    return None
