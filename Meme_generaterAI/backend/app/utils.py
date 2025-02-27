import cv2
import json
import numpy as np
import requests
# from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
from textwrap import wrap
from app.config import GROQ_API_KEY, GROQ_API_URL, UNSPLASH_API_KEY, UNSPLASH_API_URL


def fetch_image_from_unsplash(image_keywords):
    try:
        response = requests.get(UNSPLASH_API_URL, params={"query": image_keywords, "client_id": UNSPLASH_API_KEY, "per_page": 1})
        data = response.json()
        
        if "results" in data and data["results"]:
            return data["results"][0]["urls"]["regular"]
        
        print("⚠ No image found.")
        return None
    except Exception as e:
        print(f"🔥 ERROR: Unsplash API failed - {e}")
        return None








def process_text_with_groq(text):
    """Sends text to Groq AI and extracts keywords & captions."""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Extract two things from this text:\n"
                    "1. Image Keywords (1 keyword for an image search from given text)\n"
                    "2. A short, humorous meme caption\n"
                    "Return the response as valid JSON:\n"
                    "{\n"
                    '  "image_keywords": "keyword1",\n'
                    '  "meme_caption": "A funny meme caption."\n'
                    "}"
                ),
            },
            {"role": "user", "content": text},
        ],
        "max_tokens": 100,
    }

    response = requests.post(GROQ_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        if "choices" in result and result["choices"]:
            response_text = result["choices"][0].get("message", {}).get("content", "").strip()
            
            # Ensure response is in JSON format
            try:
                parsed_response = json.loads(response_text)  # ✅ Proper JSON parsing
                image_keywords = parsed_response.get("image_keywords", "funny").strip()
                print("image_keywords: ",image_keywords)
                meme_caption = parsed_response.get("meme_caption", "Funny meme!").strip()
                print("meme_caption: ",meme_caption)
                return image_keywords, meme_caption
            except json.JSONDecodeError:
                print("🔥 ERROR: Groq AI returned malformed JSON:", response_text)
        
    print(f"🔥 ERROR: Groq AI failed with status {response.status_code} - {response.text}")
    return "funny", "Funny meme!"  # Fallback values




# Generate meme caption from Groq API
# def generate_meme_caption(caption_keywords):
#     try:
#         response = requests.post(
#             GROQ_API_URL,
#             headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
#             json={
#                 "model": "llama3-70b-8192",
#                 "messages": [
#                     {"role": "system", "content": "Generate a short, witty meme caption in one sentence (max 10 words)."},
#                     {"role": "user", "content": f"Create a meme caption related to: {caption_keywords}"}
#                 ]
#             }
#         )
#         data = response.json()
#         print(f"ℹ Groq API response: {data}")
        
#         if "choices" in data and data["choices"]:
#             return data["choices"][0]["message"]["content"]
        
#         print("⚠ Groq API failed, using default caption.")
#         return "Funny meme!"
#     except Exception as e:
#         print(f"🔥 ERROR: Groq API failed - {e}")
#         return "Funny meme!"

# Dynamically adjust font size based on image width
# def get_dynamic_font(image_width):
#     base_font_size = max(50, image_width // 10)  # Scale font size dynamically
#     try:
#         return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", base_font_size)
#     except OSError:
#         print("⚠ Font not found! Using default PIL font.")
#         return ImageFont.load_default()


# Generate meme image with caption
def create_meme(image_url, caption, position="bottom"):
    if not caption:
        print("⚠ No caption received, using default.")
        caption = "Funny meme!" 
    response = requests.get(image_url)
    
    if response.status_code != 200:
        print(f"🔥 ERROR: Failed to fetch image. Status code: {response.status_code}")
        return None

    # Load image with OpenCV
    img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is None:
        print("🔥 ERROR: Image loading failed.")
        return None

    height, width, _ = img.shape

    # Dynamically adjust font size (10% of image height)
    font_scale = font_scale = height * 0.01
    font_thickness = max(1, int(font_scale * 2))

    # Get text size
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Adjust font size dynamically if text width is too large
    while True:
        (text_width, text_height), baseline = cv2.getTextSize(caption, font, font_scale, font_thickness)
        if text_width <= width * 0.9:  # Ensure text width is within 90% of image width
            break
        font_scale *= 0.95  # Reduce font scale if text is too wide
        font_thickness = max(1, int(font_scale * 2))  # Keep thickness proportional


    # Position text
    padding = int(height * 0.05)  # 5% padding from edges
    x = (width - text_width) // 2
    y = height - text_height - padding if position == "bottom" else padding + text_height

    # Ensure y is within image bounds
    y = max(padding, min(height - padding, y))


    # Add black outline for better visibility
    outline_thickness = font_thickness + 2
    for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
        cv2.putText(img, caption, (x + dx, y + dy), font, font_scale, (0, 0, 0), outline_thickness, cv2.LINE_AA)

    # Draw main caption
    cv2.putText(img, caption, (x, y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

    # Save image
    meme_path = f"app/static/memes/meme_{random.randint(1000, 9999)}.jpg"
    cv2.imwrite(meme_path, img)

    print(f"✅ Meme saved: {meme_path}")
    return meme_path