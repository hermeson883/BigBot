import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, CommandHandler, ContextTypes, ApplicationBuilder
import random
logging.basicConfig(format='(%(asctime)s - %(name)s - %(levelname)s -  %(message)s',
                    level=logging.INFO)
msgs = [
    'olá',
    'como vai',
    'de boa',
    'HI'
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o BOT, como vai?")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msgs[random.randint(0, len(msgs) - 1)])

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()