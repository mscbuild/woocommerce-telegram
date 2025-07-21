# woocommerce-telegram

# 🔧 Use Case Example

- Let’s say you want to notify users via Telegram when:

- A new order is placed

- A product is back in stock

- A customer leaves a review

# 🗂️ Project Structure
~~~bash
woocommerce-telegram-bot/
│
├── bot/
│   ├── __init__.py
│   ├── config.py
│   ├── telegram_bot.py         # Bot logic + command handlers
│   ├── woo.py                  # WooCommerce API interface
│
├── webhook/
│   ├── __init__.py
│   └── server.py               # Flask server for webhook
│
├── requirements.txt
├── run.py                      # Main entry point
└── README.md
~~~

# 🧱 Overview of What You Need

## 1. Telegram Bot
   
- Create a Telegram bot via @BotFather

- Save the bot token

## 2. WooCommerce Store

- WooCommerce REST API must be enabled

- Get your Consumer Key and Consumer Secret

## 3. Python Environment

Install required libraries:
~~~bash
pip install python-telegram-bot woocommerce flask
~~~

# 🧪 Example Use Case: Telegram Bot for New Orders

## Step 1: Basic Telegram Bot Setup (Python)

~~~bash
from telegram import Bot

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"  # Your Telegram user ID or group ID

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_telegram_message(message):
bot.send_message(chat_id=CHAT_ID, text=message)
~~~

## Step 2: WooCommerce API Integration

~~~bash
from woocommerce import API

wcapi = API(
    url="https://yourstore.com",
    consumer_key="ck_xxx",
    consumer_secret="cs_xxx",
    version="wc/v3"
)

def get_latest_orders():
    return wcapi.get("orders").json()
~~~

## Step 3: Notify on New Order (Polling or Webhook)

Option A: Polling (Not real-time, simpler)

~~~bah
import time

last_order_id = None

while True:
    orders = get_latest_orders()
    if orders:
        latest = orders[0]
        if latest['id'] != last_order_id:
            msg = f"🛒 New Order!\nCustomer: {latest['billing']['first_name']}\nTotal: {latest['total']}"
            send_telegram_message(msg)
            last_order_id = latest['id']
    time.sleep(60)
~~~

## Option B: Webhook from WooCommerce to Flask (Real-time, better)

1.Create a webhook in WooCommerce:

- Topic: Order Created

- Delivery URL: e.g., `https://yourdomain.com/webhook`

- Secret: Use something unique

- Flask app to receive webhook:
  
~~~bash
from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def wc_webhook():
    data = request.json
    msg = f"🛒 New Order!\nCustomer: {data['billing']['first_name']}\nTotal: {data['total']}"
    send_telegram_message(msg)
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
~~~

# 🧩 Optional Features

- Respond to Telegram commands (`/latest_orders`)

- Notify on stock status changes

- Add custom filters for big orders, VIP clients, etc.

# 📦 Packaging It

- Run Flask app on cloud (Heroku, Fly.io, etc.)

- Use ngrok for testing locally with webhooks:

~~~bash
ngrok http 5000
~~~

# 📁 File Contents

- `requirements.txt`
- `bot/config.py`
- `bot/woo.py`
- `bot/telegram_bot.py`
- `webhook/server.py`
- `run.py`

# 🚀 How to Run Locally

1.Install dependencies:
~~~bash
pip install -r requirements.txt
~~~
2.Start the bot:
~~~bash
python run.py
~~~
3.Run webhook server (for real-time WooCommerce updates):
~~~bash
python webhook/server.py
~~~
4.(Optional) Use ngrok to expose webhook to WooCommerce:
~~~bash
ngrok http 5000
~~~

- Then set this https://xxxx.ngrok.io/webhook as the webhook URL in your WooCommerce admin panel under:

- WooCommerce → Settings → Advanced → Webhooks

# 💬 Available Telegram Commands

| Command         | Description                |
| --------------- | -------------------------- |
| `/start`        | Greet the user             |
| `/latest_order` | Fetch latest order details |

You can add more like /stock_status, /customer_info, etc.

№№ Next you can set up Docker or deployment (Heroku, Fly.io, etc.)
