import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Perboni Pedidos está online!")


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN não encontrado nas variáveis de ambiente")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot iniciado com sucesso 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
