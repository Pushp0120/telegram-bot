import os
import telebot
from flask import Flask, request
import threading
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Get bot token from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN', '8686080430:AAFdzAYwM4hNTsyiknJMIfBFTtSOHkgn-E8')
bot = telebot.TeleBot(BOT_TOKEN)

# Admin user IDs
admin_id = ["7474658501"]

# File to store allowed user IDs
USER_FILE = "users.txt"

# File to store command logs
LOG_FILE = "log.txt"

# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to log command to the file
def log_command(user_id, command):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.datetime.now()} - {user_id}: {command}\n")

# List to store allowed user IDs
allowed_user_ids = read_users()

# Bot handlers (copy from your original m.py)
@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        bot.reply_to(message, "Welcome! The bot is ready to use.")
    else:
        bot.reply_to(message, "Access denied. You are not authorized to use this bot.")

@bot.message_handler(commands=['help'])
def help_command(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        help_text = """
        Available commands:
        /start - Start the bot
        /help - Show this help message
        """
        bot.reply_to(message, help_text)
    else:
        bot.reply_to(message, "Access denied.")

# Webhook route for Hugging Face Spaces
@app.route('/' + BOT_TOKEN, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    return '', 400

# Health check endpoint
@app.route('/')
def health_check():
    return "Bot is running!", 200

# Function to set webhook
def set_webhook():
    # In Hugging Face Spaces, the webhook URL will be your space URL + bot token
    webhook_url = f"https://{os.getenv('SPACE_NAME')}.hf.space/{BOT_TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    print(f"Webhook set to: {webhook_url}")

if __name__ == '__main__':
    # Set webhook when the app starts
    set_webhook()
    
    # Run Flask app
    app.run(host='0.0.0.0', port=7860)
