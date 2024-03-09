from telegram import Update
from telegram.ext import ContextTypes
import pyautogui as pg
import os
import time
import webbrowser
#from functools import wraps
from telegram.constants import ChatAction


username : str = "Anurag_K1603"
user_id : int = 5001467173
token_ : str = "5537989313:AAFnLJMcM9P0DQOuWBzGbDJyNviBjT8Rj6E"

async def cmd_hack(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    "Run cmd script"
    if update.effective_user.username == username and update.effective_user.id == 5001467173:
            pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False

    await update.effective_message.reply_text("Running google...")    
    
    await update.effective_message.reply_text("Running CMD hack...")
    
    os.startfile("cmd.exe")
    time.sleep(2)
    pg.write("title Hacking the system....")
    pg.press("enter")
    pg.write("prompt Hacker@AK_$g$g")
    pg.press("enter")
    pg.write("color 0a")
    pg.press("enter")
    time.sleep(2)
    pg.write("cls")
    pg.press("enter")
    await update.effective_message.reply_text("DONE.")


async def google(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    "Open google in default browser "
    if update.effective_user.username == username and update.effective_user.id == 5001467173:
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
        

async def youtube(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    "Open youtube in default browser"
    if update.effective_user.username == username and update.effective_user.id == 5001467173:
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



async def AWT(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    "Show active window title"
    if update.effective_user.username == username and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    
    
    await update.effective_message.reply_text(f"Active window : {pg.getActiveWindowTitle()}", parse_mode='Markdown')
    

async def altab(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    "Switch window"
    if update.effective_user.username == username and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
  
    
    
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")
    await update.effective_message.reply_text("Done")




async def close_sys(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    "Close current window"
    if update.effective_user.username == username and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False

    
    
    pg.keyDown("alt")
    pg.press("f4")
    pg.keyUp("alt")
    await update.effective_message.reply_text("Done")




async def shutdown(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    "Shutdown the system"
    if update.effective_user.username == username and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
 
    await update.effective_message.reply_text("Attempt to shutdown...")
    await update.effective_message.reply_text("system will shutdown after 5 seconds.")
    os.system("shutdown /s /t 1")
    


async def restart(update:Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    "Restart the system"
    if update.effective_user.username == username and update.effective_user.id == 5001467173:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False

    
    
    await update.effective_message.reply_text("Attempt to restart...")
    await update.effective_message.reply_text("system will restart after 5 seconds.")
    os.system("shutdown /r /t")
    

    
