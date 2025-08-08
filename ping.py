from flask import Flask
import requests
import threading
import time

app = Flask(__name__)

REPLIT_URL = "https://02e9e740-e15e-46e9-a4cf-f7a2cf3460d5-00-3exg0rghst83x.sisko.replit.dev/"  # 👈 Replace with your actual Replit URL

def ping_replit():
    while True:
        try:
            print("📡 Pinging Replit...")
            res = requests.get(REPLIT_URL, timeout=30)
            print("✅ Ping success:", res.status_code)
        except Exception as e:
            print("❌ Ping failed:", e)
        time.sleep(120)

@app.route("/")
def home():
    return "✅ Ping server running"

if __name__ == "__main__":
    threading.Thread(target=ping_replit, daemon=True).start()
    app.run(host="0.0.0.0", port=8080)
