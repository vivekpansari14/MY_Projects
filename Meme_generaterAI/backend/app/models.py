from pydantic import BaseModel, HttpUrl
from typing import Optional

class MemeRequest(BaseModel):
    text: str  # For Groq API
    custom_caption: Optional[str] = None

class UserUploadMemeRequest(BaseModel):
    image_url: HttpUrl
    custom_caption: str

class MemeResponse(BaseModel):
    meme_url: str
