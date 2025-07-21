from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)
from .woo import get_latest_order
from .config import TELEGRAM_BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your WooCommerce bot.")

async def latest_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order = get_latest_order()
    if order:
        name = order["billing"]["first_name"]
        total = order["total"]
        await update.message.reply_text(
            f"🛒 Latest Order\nCustomer: {name}\nTotal: ${total}"
        )
    else:
        await update.message.reply_text("No orders found.")

def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("latest_order", latest_order))
    print("✅ Telegram bot is running...")
    app.run_polling()
