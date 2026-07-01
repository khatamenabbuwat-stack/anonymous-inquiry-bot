import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    # If CHAT_ID is not set yet, do nothing (prevents crashes)
    if not CHAT_ID:
        return

    text = update.message.text

    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=f"📨 Anonymous Inquiry:\n\n{text}"
    )

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
