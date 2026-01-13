**Document360 Drive API – FastAPI Demo**
**Overview**

This project demonstrates integration with the Document360 Drive API using Python and FastAPI.
It performs end-to-end folder operations including:

Fetching all Drive folders

Creating a folder

Updating (renaming) the folder

Deleting the folder

The project follows clean structure, uses environment-based configuration, logs all requests and responses, and handles API-specific constraints.

**Tech Stack**

Python 3.11

FastAPI

Requests

python-dotenv

Logging module

**Project Structure**
Document360/
│
├── app/
│   ├── main.py                  # Application entry point
│   ├── config.py                # Environment variable loader
│   ├── logger.py                # Logging configuration
│   ├── http_client.py           # HTTP request handler
│   │
│   ├── services/
│   │   └── service.py            # Drive API operations
│   │
│   └── models/
│       └── response_validator.py # API response validation
│
├── .env                         # API token & user ID
├── requirements.txt
└── README.md

**Authentication**

API authentication is handled using the api_token header.

user_id is required for all write operations (create, update, delete).

Both values are stored securely in the .env file.

**Environment Configuration**

Create a .env file in the project root:

DOCUMENT360_API_TOKEN=your_api_token_here
DOCUMENT360_USER_ID=your_user_id_here

**Steps to Run the Project (Windows)**

Navigate to the project directory:

cd C:\Users\Lenovo\Document360


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

venv\Scripts\activate


Install dependencies:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt


Run the application:

uvicorn app.main:app --reload

**Execution Flow**

When the application starts, the following operations are executed automatically:

GET – Fetch all existing Drive folders

POST – Create a new folder

POST – Update (rename) the created folder

DELETE – Delete the folder

All requests and responses are logged in the console.

Folder Naming Convention

Initial folder name: FastAPI-Demo-Folder

Updated folder name: FastAPI-Renamed-Folder

The same folder name is used consistently across all operations and screenshots.

**Important API Notes**

Folder creation returns HTTP 200 instead of 201.

API success is determined using the "success": true flag in the response.

These API-specific behaviors are handled explicitly in the code.

**Screenshots**

Attach the following screenshots as part of the submission:

get_folders.png – Fetch folders response

Shows the GET Drive Folders API response, including existing folders, folder IDs, and metadata.
<img width="859" height="31" alt="image" src="https://github.com/user-attachments/assets/64cf7ad1-1f78-4058-8571-0aa2a8141ce4" /><br>
<img width="1567" height="658" alt="image" src="https://github.com/user-attachments/assets/7d06494c-39ee-4056-9660-00dfd73ea08a" />



create_folder.png – Folder creation response

Shows successful creation of the folder named FastAPI-Demo-Folder, along with the returned media_folder_id.
<img width="858" height="28" alt="image" src="https://github.com/user-attachments/assets/4b8ed722-a98c-434e-b3aa-dbdd40790e71" /><br>
<img width="1583" height="91" alt="image" src="https://github.com/user-attachments/assets/e25eea1a-687e-4394-98b3-540dc04288e1" />



update_folder.png – Folder update response

Shows the renaming of FastAPI-Demo-Folder to FastAPI-Renamed-Folder using the PUT method.
<img width="1250" height="54" alt="image" src="https://github.com/user-attachments/assets/ea72a61e-c883-419b-8647-0f6743563073" />


delete_folder.png – Folder deletion response

Shows successful deletion of the folder FastAPI-Renamed-Folder.
<img width="1571" height="125" alt="image" src="https://github.com/user-attachments/assets/bf00253d-28c8-424c-aebb-00fe3677c8a2" />






Summary

This project demonstrates practical backend integration with a real-world SaaS API, handling authentication, logging, validation, and API-specific constraints in a clean and structured manner.
