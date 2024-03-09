
from telegram import Update
from telegram.ext import ContextTypes
import pyautogui as pg
import os
import time
import webbrowser
#from functools import wraps
from telegram.constants import ChatAction

'''
def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    async def command_func(update: Update,context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        await context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func

    return command_func

'''


#@send_typing_action
async def cmd_hack(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    print("UUUPPPPPPDATTTTTTEEEEEEE:",update)
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    await update.effective_message.reply_text("Running CMD hack...")
    
    os.startfile("cmd.exe")
    time.sleep(2)
    pg.write("title Hacking the system....")
    pg.press("enter")
    pg.write("prompt Hacker@AK_$g$g")
    pg.press("enter")
    pg.write("color 0a")
    pg.press("enter")
    pg.write("tree")
    pg.press("enter")
    time.sleep(2)
    pg.write("cls")
    pg.press("enter")
    await update.effective_message.reply_text("DONE.")

#@send_typing_action
async def google(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    
    await update.effective_message.reply_text("Running google...")
    
    a = webbrowser.open_new_tab("google.com")
    if a:
        await update.effective_message.reply_text("Done")
    else:
        await update.effective_message.reply_text("Not able to open google")
        
#@send_typing_action
async def youtube(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    
    await update.effective_message.reply_text("Running google...")
    
    a = webbrowser.open_new_tab("youtube.com")
    if a:
        await update.effective_message.reply_text("Done")
    else:
        await update.effective_message.reply_text("Not able to open youtube")


#@send_typing_action
async def AWT(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    await update.effective_message.reply_text(f"Active window : {pg.getActiveWindowTitle()}", parse_mode='Markdown')
    

#@send_typing_action
async def altab(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")
    await update.effective_message.reply_text("Done")



#@send_typing_action
async def close_sys(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    pg.keyDown("alt")
    pg.press("f4")
    pg.keyUp("alt")
    await update.effective_message.reply_text("Done")



#@send_typing_action
async def shutdown(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    await update.effective_message.reply_text("Attempt to shutdown...")
    await update.effective_message.reply_text("system will shutdown after 5 seconds.")
    os.system("shutdown /s /t 1")
    


#@send_typing_action
async def restart(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    await update.effective_message.reply_text("Attempt to restart...")
    await update.effective_message.reply_text("system will restart after 5 seconds.")
    os.system("shutdown /r /t")
    
    


#@send_typing_action
async def sleep(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.username == "Anurag_K1603" and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    await update.effective_message.reply_text("system will sleep after 3 seconds.")
    os.system("shutdown /s /t 0")
    
    
    
