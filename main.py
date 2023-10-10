import logging
import subprocess
import os
os.system('pip install python-telegram-bot --upgrade')
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #await context.bot.send_message(chat_id=update.effective_chat.id, text="This is the output:")
    if(update.message.text == 'ls'):
        output1 = subprocess.check_output('ls', shell=True).decode('utf-8')
        print(output1)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=output1)
    elif(update.message.text == 'cd'):
        output1 = subprocess.check_output('cd', shell=True).decode('utf-8')
        print(output1)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=output1)
    elif(update.message.text == 'pwd'):
        output1 = subprocess.check_output('pwd', shell=True).decode('utf-8')
        print(output1)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=output1)
    else:
        output2 = subprocess.check_output(update.message.text, shell=True).decode('utf-8')
        print(output2)
        if(output2):
            await context.bot.send_message(chat_id=update.effective_chat.id, text=output2)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='not output')


    # await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text.upper())

    # await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text.lower())

if __name__ == '__main__':
    application = ApplicationBuilder().token('5803060145:AAG67rYEI0mvfLa6VxgzcqI0Nzs_mRu6b6Q').build()
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()
