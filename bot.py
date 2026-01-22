import os
from telegram.ext import Application, MessageHandler, CommandHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text(
        "👋 Olá! Eu sou o *Perboni Pedidos*.\n\n"
        "Envie seu pedido em texto ou áudio e eu monto para você.\n"
        "Exemplo:\n"
        "• 5 tubos 6.0\n"
        "• 2 oxidantes 20 volumes",
        parse_mode="Markdown"
    )

async def responder(update, context):
    texto = update.message.text
    await update.message.reply_text(f"Recebi: {texto}")

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN não definido")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

if __name__ == "__main__":
    main()
