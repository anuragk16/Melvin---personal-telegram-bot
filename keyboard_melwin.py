from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import ContextTypes
import pyautogui as pg
from webbrowser import open_new_tab
from setting import username,user_id


async def keyboard_mode(update:Update,context: ContextTypes.DEFAULT_TYPE):
    "Start the Keyboard Mode"
    if update.effective_user.username== username and update.effective_user.id == user_id:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False

    buttons = [
        KeyboardButton("Ctrl"),
        KeyboardButton("Alt"),
        KeyboardButton("Enter"),
        KeyboardButton("< VOL"),
        KeyboardButton("MUTE"),
        KeyboardButton("VOL >"),
        KeyboardButton("Space"),
        KeyboardButton("Shift"),
        KeyboardButton("Tab"),
        KeyboardButton("Exit"),
        KeyboardButton("<"),
        KeyboardButton("/\\"),
        KeyboardButton("\/"),
        KeyboardButton(">")
    ]
    keyboard_reply = ReplyKeyboardMarkup( [
    [buttons[0], buttons[1], buttons[2]],
    [buttons[3], buttons[4], buttons[5]],
    [buttons[6], buttons[7], buttons[8]],
    [buttons[9], buttons[10], buttons[11], buttons[12], buttons[13]]],
    resize_keyboard=True, one_time_keyboard=True)
    
    await update.effective_message.reply_text("Keyboard mode ON", reply_markup=keyboard_reply)
   
   
async def check_chat(update:Update,context: ContextTypes.DEFAULT_TYPE):
    "Reply to specific chat which include the specific string or sub-string"
    if update.effective_user.username== username and update.effective_user.id == user_id:
        pass
    else:
        await update.effective_message.reply_text("Permission denied for you ")
        return False
    
    if update.message.text == 'Ctrl': 
        pg.press("ctrl")
        await update.message.reply_text("done")
        
    elif update.message.text == 'Alt':
        pg.press("alt")
        await update.message.reply_text("done")
        
    elif update.message.text == 'Enter':
        pg.press("enter")
        await update.message.reply_text("done")
    
    elif update.message.text == '< VOL':
        pg.press("volumedown")
        await update.message.reply_text("done")
    
    elif update.message.text == 'MUTE':
        pg.press("volumemute")
        await update.message.reply_text("done")
        
    elif update.message.text == 'VOL >':
        pg.press("volumedown")
        await update.message.reply_text("done")
        
    elif update.message.text == 'Space':
        pg.press("space")
        await update.message.reply_text("done")
        
    elif update.message.text == 'Shift':
        pg.press("shift")
        await update.message.reply_text("done")
        
    elif update.message.text == 'Tab':
        pg.press("tab")
        await update.message.reply_text("done")
        
    elif update.message.text == '/\\':
        pg.press("up")
        await update.message.reply_text("done")
        
    elif update.message.text == '<':
        pg.press("left")
        await update.message.reply_text("done")
        
    elif update.message.text == '>':
        pg.press("right")
        await update.message.reply_text("done")
        
    elif update.message.text == '\/':
        pg.press("down")
        await update.message.reply_text("done")
    
    elif update.message.text == 'Exit':
        await update.message.reply_text("Exit keyboard mode!!", reply_markup=ReplyKeyboardRemove())


    elif update.message.text[0:2] == "GS":
        text = update.message.text.split(" ")
        text.pop(0)
        text = "+".join(text)
        open_new_tab(f"https://www.google.com/search?q={text}")
        await update.message.reply_text("google search done")
    
    elif update.message.text[0:2] == "YS":
        text = update.message.text.split(" ")
        text.pop(0)
        text = "+".join(text)
        open_new_tab(f"https://www.youtube.com/search?q={text}")
        await update.message.reply_text("google search command")

    elif update.message.text[0:4] == 'TYPE':
        text = update.message.text.split(" ")
        text.pop(0)
        text = " ".join(text)
        pg.typewrite(text)
        await update.message.reply_text("done")

    """
    else: 
        await update.message.reply_text(f"Your message is: {update.message.text}") 
    """
