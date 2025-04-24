from fastapi import APIRouter, HTTPException, Query
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/pexels", tags=["Pexels"])

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
PEXELS_BASE_URL = "https://api.pexels.com/v1/search"

@router.get("/images")
def get_pexels_images(query: str = Query(...), per_page: int = 10):
    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": per_page
    }

    response = requests.get(PEXELS_BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Pexels API failed.")

    return response.json()
