from app.http_client import send_request
from app.config import BASE_URL
from app.models.response_validator import validate_response
from app.logger import logger
from app.config import USER_ID

stored_folder_id = None


def get_all_folders():
    response = send_request("GET", BASE_URL)
    validate_response(response, 200)

    logger.info("Fetched all folders successfully")
    logger.info(response.text)
    return response.text


def create_folder(folder_name, parent_id=None):
    global stored_folder_id

    payload = {
        "title": folder_name,
        "user_id": USER_ID
    }

    response = send_request("POST", BASE_URL, payload)
    validate_response(response, allowed_statuses=(200, 201))

    data = response.json()["data"]
    stored_folder_id = data["media_folder_id"]

    logger.info(f"Folder created → ID: {stored_folder_id}")
    return stored_folder_id


def update_folder(folder_id, new_name):
    if not folder_id:
        raise ValueError("Folder ID is None. Cannot update folder.")

    url = f"{BASE_URL}/{folder_id}"

    payload = {
        "title": new_name,
        "user_id": USER_ID
    }

    response = send_request("POST", url, payload)
    validate_response(response, allowed_statuses=(200,))

    logger.info("Folder name updated successfully")



def delete_folder(folder_id):
    url = f"{BASE_URL}/{folder_id}"

    payload = {
        "user_id": USER_ID
    }

    response = send_request("DELETE", url, payload)
    validate_response(response, allowed_statuses=(200, 201))


    logger.info("Folder deleted successfully")

