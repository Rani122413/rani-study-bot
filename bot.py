import os
import telebot
import datetime
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """🔥 **Rani Study Bot Live hai 24x7!**
    
Commands:
/time - Time dekho
/joke - Joke suno
/start - Welcome msg""", parse_mode="Markdown")

@bot.message_handler(commands=['time'])
def time(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    bot.reply_to(message, f"⏰ Abhi ka time: `{now}`", parse_mode="Markdown")

@bot.message_handler(commands=['joke'])
def joke(message):
    jokes = [
        "Teacher: Homework kaha hai? \nStudent: Kutta kha gaya 😂",
        "Main: Bhook lagi \nMummy: Padhai kar le"
    ]
    bot.reply_to(message, random.choice(jokes))

print("Bot Live on Railway")
bot.infinity_polling()
