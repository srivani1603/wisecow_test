import requests
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Application URL
APP_URL = 'http://example.com'

def check_application_health():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            logging.info(f'Application is up. Status code: {response.status_code}')
        else:
            logging.warning(f'Application is down. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error checking application health: {e}')

if __name__ == "__main__":
    check_application_health()
    print("Application health check complete. Check 'app_health.log' for details.")
