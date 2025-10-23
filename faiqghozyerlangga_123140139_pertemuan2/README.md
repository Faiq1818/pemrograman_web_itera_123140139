# Aplikasi Dashboard Pribadi

## Fitur Utama

- Menambahkan, menandai dan menghapus todolist
- Penyimpanan data otomatis di browser
- Menampilkan data cuaca dan suhu sekarang

## Screenshot Aplikasi
#### Tampilan dasar
![Screenshot 1](./screenshots/screenshot1.png)

#### Menampilkan todolist yg didapat dari localstorage atau ditambahkan langsung
![Screenshot 2](./screenshots/screenshot2.png)

#### List bisa ditandai selesai
![Screenshot 3](./screenshots/screenshot3.png)

## Cara Menjalankan Aplikasi

1. Clone repository:
   ```
   git clone https://github.com/Faiq1818/pemrograman_web_itera_123140139.git
   ```
2. Masuk ke folder tugasnya
   ```
   cd pemrograman_web_itera_123140139/faiqghozyerlangga_123140139_pertemuan2
   ```
3. Install dependensi
   ```
   npm install
   ```
4. Jalankan localhost
   ```
   npm run start
   ```
5. Browser otomatis terbuka atau cek di localhost:8080

## Pengguanan fitur ES6+
1. let dan const

penggunaan fitur ini sangat umum di kode saya ini, berikut contohnya:
#### js/todolist.js
```js
  const saveTasks = () => {
    const tasks = [];
    list.querySelectorAll("li").forEach((li) => {
      let text = li.querySelector("span").textContent.trim();
      let completed = li.querySelector("input[type='checkbox']").checked;
      tasks.push({ text, completed });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
  };
```
2. Arrow function dan async await

Fitur arrow function sangat berguna untuk fungsi yg hanya digunakan sekali saja, lalu untuk async await sangat berguna untuk penggunaan asynchronous yg menunggu suatu data atau komputasi selesai sebelum melanjutkan kode, berikut ini adalah contohnya, saya menggunakan async await untuk fetching api data cuaca dari open-meteo: 
##### js/weather.js
```js
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
```
3. Template literal

Fitur berguna untuk fleksibilitas dan kemudahan dalam memasukan variabel ke dalam suatu string:
##### js/weather.js
```js
  const renderWeather = (data) => {
    const temperature = document.getElementById("temperature");
    const place = document.getElementById("place");
    const weather = document.getElementById("weather");

    place.innerHTML = "Bandar Lampung";
    temperature.innerHTML = `${data.current_weather.temperature}°C`;
```
4. Class

Walaupun jarang digunakan oleh kebanyakan developer frontend javascript, class masih tetap bisa digunakan untuk mengenkapsulasi suatu kode, berikut contohnya:
##### js/weather.js
```js
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
```

