# 💓 Hyperate Heart Rate Monitor (Python)

This script monitors your heart rate in real time using the [Hyperate](https://app.hyperate.io) web platform and displays the heart rate both in the Terminal and the Command Prompt Window Title.

## 📦 Requirements

Make sure you have Python 3.7 or later installed. Then, install the required Python packages:

```bash
pip install selenium webdriver-manager
```
```bash
pip install colorama
```

## 🖥️ How It Works

The script:
1. Launches a headless Chrome browser.
2. Connects to your **Hyperate Live Session** URL.
3. Reads the current heart rate displayed on the page.
4. Displays the BPM in:
   - The Terminal (with a timestamp)
   - The CMD Window title like: `Heartrate Monitor - 100BPM`
5. Updates every 6 seconds.

## 🩺 How to Set Up Hyperate

1. Download Hyperate from your preferred App Store, This works on iOS Android, Android Watch, Garmin, and Fitbit. For this Tutorial I'll be using a Apple Watch.
2. Open the App and Start session.
3. Copy your unique session URL — it looks like: 'https://app.hyperate.io/exampleid'
4. Locate the line that says `'url = https://app.hyperate.io/IDHERE'` and replace IDHERE with your own Hyperate session ID.
5. Save changes then run the Code!

## ❤️ Heartrate Categories

| Category  | BPM Range | Description                     | Color         |
|-----------|-----------|---------------------------------|---------------|
| LOW       | 0 - 65    | Resting / Low activity          | 🔵 Blue       |
| MODERATE  | 66 - 130  | Light activity / Normal range   | 🟢 Green      |
| MEDIUM    | 131 - 155 | Moderate exercise intensity     | 🟡 Yellow     |
| HIGH      | 156 - 180 | High-intensity activity         | 🔴 Red        |
| VERY HIGH | 181 - 240 | Extreme exertion / Peak rate    | 🔴 Red        |

## 🚨 Disclaimer
This script is intended for personal use only and is not a substitute for medical advice. It utilizes publicly available data from your Hyperate session to monitor heart rate.

Please note that this program is not designed to detect medical conditions such as heart attacks. If you experience any symptoms of distress, please seek immediate assistance from a healthcare professional or contact emergency services.

Made with ❤️ by fraudian
