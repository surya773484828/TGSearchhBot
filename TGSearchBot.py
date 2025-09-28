from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Get token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Channels
CHANNELS = [
    {"text": "Channel 1", "url": "https://youtube.com/@ambarstoryuniverse"},
    {"text": "Channel 2", "url": "https://t.me/LootPeLootDealsOfficial"},
    {"text": "Channel 3", "url": "https://t.me/AmbarStoryUniverseOfficial"},
]

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for ch in CHANNELS:
        keyboard.append([InlineKeyboardButton(ch["text"], url=ch["url"])])

    keyboard.append([InlineKeyboardButton("I have joined / Verify", callback_data="verify")])
    keyboard.append([InlineKeyboardButton("Refer & Earn", callback_data="refer")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        """ Welcome! 🎯
This is TGSearch Bot.
Type any search word (e.g. "music", "news") and I’ll show results.

𝐒𝐡𝐚𝐫𝐞 𝐓𝐆𝐬𝐞𝐚𝐫𝐜𝐡 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝟏𝟎 𝐏𝐞𝐫𝐬𝐨𝐧𝐬.
𝐘𝐨𝐮 𝐰𝐢𝐥𝐥 𝐄𝐚𝐫𝐧 𝟐𝟎/- 𝐩𝐞𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥.
𝐌𝐢𝐧𝐢𝐦𝐮𝐦 𝐰𝐢𝐭𝐡𝐝𝐫𝐚𝐰𝐚𝐥 𝐚𝐦𝐨𝐮𝐧𝐭 𝐢𝐬 𝟐𝟎𝟎/-

𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟𝗦 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧""",
        reply_markup=reply_markup
    )

# Button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "verify":
        all_joined = True
        # Check only Telegram channels (skip YouTube)
        for ch in CHANNELS[1:]:
            chat_id = ch["url"].replace("https://t.me/", "@")
            try:
                member = await context.bot.get_chat_member(chat_id=chat_id, user_id=query.from_user.id)
                if member.status in ["left", "kicked"]:
                    all_joined = False
                    break
            except:
                all_joined = False
                break

        if all_joined:
            await query.edit_message_text(
                "✅ Verified! Click the link and start searching: https://t.me/OKSearch?start=8286109879"
            )
        else:
            await query.answer("⚠ Please join all channels first!", show_alert=True)

    elif query.data == "refer":
        await query.edit_message_text(
            """(Copy This Message And Share To Refer)
📌 टेलीग्राम का सब कुछ मिलेगा सेकंड्स में!
TGsearch Bot से कोई भी Story, Movie, Anime, Leacture या Course सबकुछ तुरंत ढूंढो। 😍
💰 Refer & Earn से बढ़िया पैसे भी कमाओ। जल्दी फायदा उठाओ और दोस्तों को भी बताओ!
👉@tgsearchingg_Bot"""
        )

# Main
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
