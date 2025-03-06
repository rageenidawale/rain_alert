# 🌦 Rain Alert App ☂️  

A Python-based weather alert system that notifies you via **SMS and WhatsApp** if it's going to rain in your area.

---

## ✨ Features  
- Fetches **hourly weather data** from OpenWeather API.  
- Checks if rain is expected in the next **12 hours**.  
- Sends **SMS and WhatsApp alerts** using Twilio.  

---

## 🛠 Setup Instructions  

### 1️⃣ Install Dependencies  

Ensure Python is installed, then install required libraries:  

```bash
pip install requests twilio
```

---

### 2️⃣ Get API Keys  

- Sign up for **[OpenWeather API](https://openweathermap.org/api)** and get an API Key.  
- Create a **[Twilio](https://www.twilio.com/)** account and get:  
  - `ACCOUNT_SID`  
  - `AUTH_TOKEN`  
  - `FROM_NUMBER` (Twilio phone number)  
  - `WHATSAPP_PHONE_NUMBER` (for WhatsApp messages)  

---

### 3️⃣ Configure API Keys  

In `main.py`, replace the placeholders with your credentials:  

```python
API_KEY = "your_openweather_api_key"
ACCOUNT_SID = "your_twilio_account_sid"
AUTH_TOKEN = "your_twilio_auth_token"
FROM_NUMBER = "your_twilio_phone_number"
TO_NUMBER = "your_phone_number"
WHATSAPP_PHONE_NUMBER = "your_twilio_whatsapp_number"
```

---

### 4️⃣ Run the Application  

Execute the script:  

```bash
python main.py
```

If rain is expected in the next **12 hours**, you'll receive an **SMS & WhatsApp alert**.

---

## 📜 How It Works  

1. Fetches **hourly weather forecast** using **OpenWeather API**.  
2. Checks if any weather condition indicates **rain** (`weather ID < 700`).  
3. If rain is detected, sends a **Twilio SMS & WhatsApp message**.  
