from fastapi import APIRouter
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
API_KEY = os.getenv("CLOUDINARY_API_KEY")
API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

print("CLOUDINARY_CLOUD_NAME =", CLOUD_NAME)
print("CLOUDINARY_API_KEY =", API_KEY) 
print("CLOUDINARY_API_SECRET =", API_SECRET)

@router.get("/cloudinary/images/{folder}")
def get_images_by_folder(folder: str):
    print(f"Fetching images for folder: {folder}")
    url = f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/resources/search"
    expression = f'folder="{folder}"'
    
    response = requests.post(
        url,
        auth=HTTPBasicAuth(API_KEY, API_SECRET),
        json={"expression": expression},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        print(f"FAILED: {response.status_code} - {response.text}")
        return {"error": "Failed to fetch from Cloudinary"}
    
    
    return response.json()
