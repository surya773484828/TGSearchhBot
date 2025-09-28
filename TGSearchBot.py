from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CHANNELS = [
    {"text": "Channel 1", "url": "https://youtube.com/@ambarstoryuniverse"},
    {"text": "Channel 2", "url": "https://t.me/LootPeLootDealsOfficial"},
    {"text": "Channel 3", "url": "https://t.me/AmbarStoryUniverseOfficial"},
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for ch in CHANNELS:
        keyboard.append([InlineKeyboardButton(ch["text"], url=ch["url"])])

    keyboard.append([InlineKeyboardButton("I have joined / Verify", callback_data="verify")])
    keyboard.append([InlineKeyboardButton("Refer & Earn", callback_data="refer")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! 🎯 This is TGSearch Bot.\nType any search word (e.g., 'music', 'news') and I’ll show results.",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "verify":
        await query.edit_message_text(
            "✅ Verified! Click the link and start searching: https://t.me/OKSearch?start=8286109879"
        )
    elif query.data == "refer":
        await query.edit_message_text(
            "📌 TGSearch Bot: Search Story, Movie, Anime, Lectures, Courses instantly! 😍\n"
            "💰 Refer & Earn (just for publicity)!\n"
            "Share with your friends: 👉@tgsearchingg_Bot"
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
