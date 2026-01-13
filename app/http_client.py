import requests
from app.config import API_TOKEN
from app.logger import logger

HEADERS = {
    "api_token": API_TOKEN,
    "Content-Type": "application/json"
}

TIMEOUT = 10


def send_request(method, url, payload=None):
    try:
        logger.info(f"REQUEST {method} → {url}")
        logger.info(f"HEADERS → {HEADERS}")
        logger.info(f"BODY → {payload}")

        response = requests.request(
            method=method,
            url=url,
            headers=HEADERS,
            json=payload,
            timeout=TIMEOUT
        )

        logger.info(f"STATUS → {response.status_code}")
        logger.info(f"RAW RESPONSE → {response.text}")

        return response

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        raise

    except requests.exceptions.RequestException as e:
        logger.error(f"HTTP Error: {str(e)}")
        raise
