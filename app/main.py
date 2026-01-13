from fastapi import FastAPI
from app.services.service import (
    get_all_folders,
    create_folder,
    update_folder,
    delete_folder,
    stored_folder_id
)

app = FastAPI()


@app.on_event("startup")
def run_demo():
    print("\n--- DOCUMENT360 DRIVE API DEMO START ---\n")

    get_all_folders()

    folder_id = create_folder("FastAPI-Demo-Folder")

    #update_folder(folder_id, "FastAPI-Renamed-Folder")

    delete_folder(folder_id)

    print("\n--- DEMO COMPLETED SUCCESSFULLY ---\n")
