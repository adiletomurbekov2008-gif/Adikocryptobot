import os
import time
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

EXCHANGES = {
    "binance": "https://api.binance.com/api/v3/ticker/price",
    "bybit": "https://api.bybit.com/v5/market/tickers?category=spot",
    "okx": "https://www.okx.com/api/v5/market/tickers?instType=SPOT",
    "kucoin": "https://api.kucoin.com/api/v1/market/allTickers",
    "bitget": "https://api.bitget.com/api/spot/v1/market/tickers",
    "gate": "https://api.gateio.ws/api/v4/spot/tickers"
}

def get_prices(symbol):
    prices = {}
    try:
        prices["Binance"] = requests.get(EXCHANGES["binance"]).json()
    except:
        pass
    return prices

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Отправь название монеты (например: BTCUSDT)\n"
        "Я покажу разницу цен на биржах."
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = update.message.text.upper()
    await update.message.reply_text(
        f"🔍 Ищу цены для {symbol}\n(упрощённая версия, тест)"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()
