import json
import requests

# URL to check
TARGET_URL = "https://example.com"  # Replace with your target URL

def check_url():
    try:
        response = requests.get(TARGET_URL)
        status_code = response.status_code
        response_body = response.text
    except Exception as e:
        status_code = 500
        response_body = f"An error occurred: {e}"

    return status_code, response_body

def handler(request):
    # Extract endpoint path from request
    path = request.get("path", "")

    if path == "/status":
        # Check URL status and respond
        status_code, response_body = check_url()
        
        result = {
            "status": "success",
            "message": "URL status checked.",
            "target_url_status_code": status_code,
            "target_url_response": response_body
        }

        return {
            "statusCode": 200,
            "body": json.dumps(result),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    else:
        # Default response for other endpoints
        return {
            "statusCode": 404,
            "body": json.dumps({"status": "error", "message": "Endpoint not found."}),
            "headers": {
                "Content-Type": "application/json"
            }
        }
      
