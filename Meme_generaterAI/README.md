# 🎭 AI-Based Meme Generator

## 🚀 Overview
The AI-Based Meme Generator is a full-stack web application that dynamically generates humorous memes using AI-powered captioning and relevant image fetching. It utilizes **FastAPI** for the backend and **React** for the frontend, integrating the **Unsplash API** to fetch images and the **Groq API** to generate meme captions.

## ✨ Features
- 🔍 **AI-Powered Captioning** – Uses Groq AI to generate witty and contextually relevant meme captions.
- 🖼 **Smart Image Selection** – Fetches images from Unsplash based on keyword analysis and strict filtering.
- 📤 **User Customization** – Allows users to upload their own images and modify captions.
- ⚡ **FastAPI Backend** – Ensures high-performance API responses for quick meme generation.
- 🎨 **React Frontend** – Provides an intuitive and seamless user interface.
- 📥 **Downloadable Memes** – Users can download their generated memes with a single click.

## 🏗 Tech Stack
- **Backend:** FastAPI, Python, Unsplash API, Groq API
- **Frontend:** React, Tailwind CSS
- **Database (if needed):** SQLite / PostgreSQL

## 🔧 Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/ai-meme-generator.git
cd ai-meme-generator
```
### **2️⃣ Set Up Virtual Environment (Backend)**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```
### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and add:
```ini
UNSPLASH_API_KEY=your_unsplash_api_key
GROQ_API_KEY=your_groq_api_key
```

### **5️⃣ Run the FastAPI Server**
```bash
uvicorn app.main:app --reload
```

### **6️⃣ Start the Frontend (React)**
```bash
cd frontend
npm install
npm start
```

## 🛠 API Endpoints
### **1️⃣ Generate a Meme**
```http
POST /generate-meme
```
#### **Request Body:**
```json
{
  "text": "Being superman is a hard job, Batman got it easy.",
  "custom_caption": ""
}
```
#### **Response:**
```json
{
  "image_url": "https://unsplash.com/photos/superman-flying.jpg",
  "meme_caption": "When you thought being a superhero was easy...",
  "meme_url": "http://localhost:8000/memes/meme_1234.jpg"
}
```

## 🤝 Contribution
Feel free to fork the repo, submit issues, and contribute to improvements! PRs are welcome. 🎉

## 📜 License
This project is licensed under the MIT License.

---

🚀 **Enjoy generating memes with AI!**

