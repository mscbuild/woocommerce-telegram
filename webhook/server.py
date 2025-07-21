from flask import Flask, request
from bot.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from telegram import Bot

app = Flask(__name__)
bot = Bot(token=TELEGRAM_BOT_TOKEN)

@app.route("/webhook", methods=["POST"])
def wc_webhook():
    data = request.json
    if not data:
        return "No data", 400

    name = data["billing"]["first_name"]
    total = data["total"]
    msg = f"📦 New WooCommerce Order\nCustomer: {name}\nTotal: ${total}"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)
    return "OK", 200
