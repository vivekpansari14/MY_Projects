from fastapi import APIRouter, HTTPException
import os
from fastapi.responses import JSONResponse
from app.models import MemeRequest, MemeResponse
from app.utils import fetch_image_from_unsplash, create_meme, process_text_with_groq

router = APIRouter()

BASE_URL = "http://127.0.0.1:8000"  # Change when deploying


@router.post("/generate-meme", response_model=MemeResponse)
async def generate_meme_endpoint(request: MemeRequest):
    print(f"ℹ Received request: {request.dict()}")  # Debugging log

    try:
        # Process text using Groq AI
        image_keywords, meme_caption = process_text_with_groq(request.text)
        if not image_keywords:
            raise ValueError("Failed to extract keywords from text.")

        # Fetch image from Unsplash From AI generated keywords
        image_url = fetch_image_from_unsplash(image_keywords)
        if not image_url:
            raise ValueError("Could not fetch an image from Unsplash.")

        caption = request.custom_caption or meme_caption

        # Create meme
        meme_path = create_meme(image_url, caption)

        # Convert file path to URL
        meme_filename = os.path.basename(meme_path)
        meme_url = f"{BASE_URL}/memes/{meme_filename}"

        print(f"✅ Meme generated: {meme_url}")  # Debugging log
        return {"meme_url": meme_url}
    
    except Exception as e:
        print(f"🔥 ERROR: {str(e)}")
        return JSONResponse(status_code=500, content={"detail": "Failed to generate meme"})
