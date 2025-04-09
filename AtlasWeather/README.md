
# 🌍 AtlasWeather

AtlasWeather is a sleek, map-based weather application that combines the power of the Google Maps API and the OpenWeatherMap API to provide real-time weather data based on user-entered locations.

---

## 🔧 Features

- 📍 Real-time location-based weather updates
- 🗺 Interactive Google Map integration
- 🌤 Temperature, humidity, and wind data
- ❗ Error handling for empty inputs, API issues, and invalid responses
- 💅 Sleek modern UI using HTML, CSS, JavaScript, and Bootstrap 5

---

## 📁 Project Structure

```
/frontend
├── index.html         # Main UI page
├── styles.css         # Styling for UI
└── script.js          # JavaScript for API calls & Map rendering

/backend
└── app.py             # Flask app handling the /weather route

.env                   # Store your API keys securely
```

---

## ⚙️ Setup Instructions

1. **Clone the project**:

```bash
git clone https://github.com/yourusername/atlasweather.git
cd atlasweather
```

2. **Set up the backend (Flask)**:

```bash
pip install flask python-dotenv requests
```

3. **Create a `.env` file** in the root directory and add:

```
GOOGLE_API_KEY=your_google_maps_api_key
WEATHER_API_KEY=your_openweathermap_api_key
```

4. **Run the Flask backend**:

```bash
python app.py
```

5. **Open `index.html` in your browser** or serve with Flask static files.

---

## 📝 Notes

- Ensure the backend is running on `http://localhost:5000`.
- Make sure to replace API key placeholders.
- Cross-Origin issues? Serve frontend via Flask or set up CORS.

---

## 📄 License

MIT
