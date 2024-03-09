
import logging
from telegram import Update , InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from setting import  cmd_hack, google, youtube, close_sys, AWT, altab, shutdown, restart, sleep  #send_typing_action
from keyboard_melwin import keyboard_mode, check_rp
import telegram
from time import sleep

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


#@send_typing_action
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  
    print(update.message.from_user["username"])
    print(update.message.from_user["id"])
    if update.message.from_user["username"] == "Anurag_K1603" and update.message.from_user["id"] == 5001467173:
        

        await update.message.reply_text("Hello friends, This is melvin :>] , programed by anurag kumawat\
            .Please write /help to see the commands available.")
        return True
        
    else:
        await update.message.reply_text("Hello friends, This is melvin :>] , programed by anurag kumawat\
            .\n YOU ARE NOT AUTHORIZED BY ANURAG TO USE THIS BOT - HAHAHA ")
        return False
    

        

#@send_typing_action
async def help(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:

    # Create a list of buttons
    buttons = [
        InlineKeyboardButton("Google", callback_data="google"),
        InlineKeyboardButton("Youtube", callback_data="youtube"),
        InlineKeyboardButton("CMD hack", callback_data="cmd_hack"),
        InlineKeyboardButton("AWT", callback_data="awt"),
        InlineKeyboardButton("Switch tab", callback_data="altab"),
        InlineKeyboardButton("Close window", callback_data="close_sys"),
        InlineKeyboardButton("Restart", callback_data="restart"),
        InlineKeyboardButton("Shutdown", callback_data="shutdown"),
        InlineKeyboardButton("* KEYBOARD MODE *", callback_data="keyboard_mode")

    ]

    # Create the markup
    markup = InlineKeyboardMarkup([
    [buttons[0], buttons[1]],[ buttons[2], buttons[3]],
    [buttons[4], buttons[5]],[ buttons[6], buttons[7]],
    [buttons[8]]
])
    
    await update.message.reply_text("Available Commands :-",reply_markup=markup)
    



def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    
  
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("cmd_hack", cmd_hack))
    application.add_handler(CommandHandler("google", google))
    application.add_handler(CommandHandler("awt", AWT))
    application.add_handler(CommandHandler("altab", altab))
    application.add_handler(CommandHandler("shutdown", shutdown))
    application.add_handler(CommandHandler("close_sys", close_sys))
    application.add_handler(CommandHandler("restart", restart))
    application.add_handler(CommandHandler("youtube", youtube))
    application.add_handler(CommandHandler("keyboard_mode", keyboard_mode))
    
    
    
    application.add_handler(CallbackQueryHandler(google, "google"))
    application.add_handler(CallbackQueryHandler(youtube, "youtube"))
    application.add_handler(CallbackQueryHandler(cmd_hack, "cmd_hack"))
    application.add_handler(CallbackQueryHandler(AWT, "awt"))
    application.add_handler(CallbackQueryHandler(altab, "altab"))
    application.add_handler(CallbackQueryHandler(close_sys, "close_sys"))
    application.add_handler(CallbackQueryHandler(restart, "restart"))
    application.add_handler(CallbackQueryHandler(shutdown, "shutdown"))
    application.add_handler(CallbackQueryHandler(keyboard_mode, "keyboard_mode"))
    
    
    application.add_handler(MessageHandler(filters.CHAT, check_rp))
    
    application.run_polling()
    
    


if __name__ == "__main__":
    
    
    application = Application.builder().token("5537989313:AAFnLJMcM9P0DQOuWBzGbDJyNviBjT8Rj6E").build()
    
    main()
    
    
