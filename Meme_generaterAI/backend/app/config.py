import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# API Keys (stored securely in .env file)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY")

# API URLs
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"

# Other settings
IMAGE_DOWNLOAD_FOLDER = "app/static/memes"
ALLOWED_IMAGE_FORMATS = {"png", "jpg", "jpeg"}

# Ensure the image download folder exists
if not os.path.exists(IMAGE_DOWNLOAD_FOLDER):
    os.makedirs(IMAGE_DOWNLOAD_FOLDER)
