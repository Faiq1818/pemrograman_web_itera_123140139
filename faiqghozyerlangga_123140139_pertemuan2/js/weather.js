class WeatherDescription {
  constructor(code) {
    this.code = code;
  }

  getDescription() {
    switch (this.code) {
      case 0:
        return "☀️ Cerah";
      case 1:
        return "🌤️ Sebagian besar cerah";
      case 2:
        return "⛅ Sebagian berawan";
      case 3:
        return "☁️ Berawan";
      case 45:
        return "🌫️ Kabut";
      case 48:
        return "🌫️ Kabut beku";
      case 51:
        return "🌦️ Gerimis ringan";
      case 53:
        return "🌧️ Gerimis sedang";
      case 55:
        return "🌧️ Gerimis lebat";
      case 61:
        return "🌦️ Hujan ringan";
      case 63:
        return "🌧️ Hujan sedang";
      case 65:
        return "🌧️ Hujan lebat";
      case 80:
        return "🌦️ Hujan badai ringan";
      case 81:
        return "⛈️ Hujan badai sedang";
      case 82:
        return "⛈️ Hujan badai kuat";
      default:
        return "🌍 Tidak diketahui";
    }
  }
}

export default function Weather() {
  //fetch the weather api 
  const getWeather = async () => {
    // Bandar Lampung coordinate
    const lat = -5.4264;
    const lon = 105.2610;
    const url =
      `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

    try {
      const res = await fetch(url);
      const data = await res.json();
      //render weather after getting the data from api
      renderWeather(data);
    } catch (err) {
      console.error(err);
    }
  };

  const renderWeather = (data) => {
    const temperature = document.getElementById("temperature");
    const place = document.getElementById("place");
    const weather = document.getElementById("weather");

    place.innerHTML = "Bandar Lampung";
    temperature.innerHTML = `${data.current_weather.temperature}°C`;
    
    //returning the case from weathercode
    const weatherDesc = new WeatherDescription(
      data.current_weather.weathercode,
    );
    //and render it
    weather.innerHTML = weatherDesc.getDescription();
  };

  getWeather();
}
