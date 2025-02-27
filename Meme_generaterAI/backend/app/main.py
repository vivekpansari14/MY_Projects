from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="AI Meme Generator")

# Include API routes
app.include_router(router)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEME_DIR = os.path.join(BASE_DIR, "static/memes")

@app.get("/")
def root():
    return {"message": "Welcome to the AI Meme Generator API!"}

print(f"ℹ Mounting memes directory: {MEME_DIR}")  # Debugging output

# Mount static files correctly
app.mount("/memes", StaticFiles(directory=MEME_DIR), name="memes")