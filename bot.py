from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import asyncio
import os

TOKEN = "8828897286:AAFxLx_eamjChGEgXwfdYItNnGegMdQOhNM"

DELETE_AFTER = 7200  # 2 ساعت (به ثانیه)

async def delete_message_later(app, chat_id, message_id):
    await asyncio.sleep(DELETE_AFTER)
    try:
        await app.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except:
        pass

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        msg = update.channel_post

        context.application.create_task(
            delete_message_later(
                context.application,
                msg.chat_id,
                msg.message_id
            )
        )

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POSTS, handler))

app.run_polling()
