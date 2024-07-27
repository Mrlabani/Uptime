from flask import Flask, jsonify
import requests
import time
import logging
from threading import Thread

# Configuration
TARGET_URL = 'https://064340c9-5b89-4dcb-9b5b-bcf49ef1665a-00-329qi2ydkhy9u.pike.replit.dev'  # Replace with your target URL
CHECK_INTERVAL = 60  # Check every 60 seconds

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_url_status(url):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout to prevent hanging
        if response.status_code == 200:
            logging.info(f"URL is up. Status code: {response.status_code}")
        else:
            logging.warning(f"URL is down. Status code: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")

def monitor_url(url, interval):
    while True:
        check_url_status(url)
        time.sleep(interval)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Koyeb Is Running...."})

def run_flask():
    app.run(host='0.0.0.0', port=8080)  # Use port 8080 for Koyeb

if __name__ == "__main__":
    # Start monitoring URL in a separate thread
    monitor_thread = Thread(target=monitor_url, args=(TARGET_URL, CHECK_INTERVAL))
    monitor_thread.daemon = True
    monitor_thread.start()

    # Run Flask app
    run_flask()
  
