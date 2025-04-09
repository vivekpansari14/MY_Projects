// script.js
const form = document.getElementById('weatherForm');
const weatherResult = document.getElementById('weatherResult');
const locationInput = document.getElementById('locationInput');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const location = locationInput.value.trim();

  if (!location) {
    showError("Please enter a location.");
    return;
  }

  try {
    const res = await fetch(`http://localhost:5000/weather?location=${encodeURIComponent(location)}`);

    if (!res.ok) {
      const errorText = await res.text();
      throw new Error(`Server responded with status ${res.status}: ${errorText}`);
    }

    const data = await res.json();

    if (data.status === 'success') {
      const { weather, lat, lon } = data;

      weatherResult.classList.remove('d-none');
      weatherResult.innerHTML = `
        <h4 class="fw-semibold">📍 Weather in <span class="text-primary">${weather.name}</span></h4>
        <hr>
        <p><strong>${weather.weather[0].main}</strong> - ${weather.weather[0].description}</p>
        <p>🌡 Temperature: <strong>${weather.main.temp} °C</strong></p>
        <p>💧 Humidity: <strong>${weather.main.humidity}%</strong></p>
        <p>🌬 Wind Speed: <strong>${weather.wind.speed} m/s</strong></p>
      `;

      const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: { lat, lng: lon },
        mapTypeControl: false,
        streetViewControl: false,
      });

      new google.maps.Marker({ position: { lat, lng: lon }, map });
    } else {
      showError(data.message || "Location not found.");
    }
  } catch (error) {
    showError(`Error fetching weather: ${error.message}`);
  }
});

function showError(message) {
  weatherResult.classList.remove('d-none');
  weatherResult.innerHTML = `<p class="text-danger fw-semibold">❗ ${message}</p>`;
}
