from twilio.rest import Client
import schedule
import time
import os
from dotenv import load_dotenv
from flask import Flask
import threading

# Load environment variables from .env file
load_dotenv()


# Twilio credentials
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio sandbox number
RECIPIENT_NUMBERS = [
    'whatsapp:+2347071237007',
    'whatsapp:+2347038368366' # Add as many numbers as needed
]

# Verify that the credentials are loaded
if not ACCOUNT_SID or not AUTH_TOKEN:
    raise ValueError("Twilio credentials are not set in the environment variables.")

# Create Twilio clien
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Define messages
message_a =["NO MORE INTERNS !!!!!",
            "NO MORE LOANS OR EXTENDED FAMILY HELP !!!!",
            "NO MORE CRYPTO BORROWING !!!!",
            "NO MORE STARTUP INVESTMENTS !!!!"]
message_b = "Don't forget to check up on FAMILY (Mom, Dad, KC, Chiggy, Chi, and Donald)"


# Flask web server
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def run_web_server():
    print("Starting web server...")
    app.run(host='0.0.0.0', port=8080)


# Function to send WhatsApp messages
def send_whatsapp_message(message):
    try:
        client.messages.create(
            from_=WHATSAPP_NUMBER,
            to=RECIPIENT_NUMBERS,
            body=message
        )
        print(f"Message sent: {message}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Schedule messages
def schedule_messages():
    # Weekdays (Monday to Friday)
    schedule.every().monday.at("08:00").do(lambda: send_whatsapp_message(message_a))
    schedule.every().tuesday.at("08:00").do(lambda: send_whatsapp_message(message_a))
    schedule.every().wednesday.at("08:00").do(lambda: send_whatsapp_message(message_a))
    schedule.every().thursday.at("08:00").do(lambda: send_whatsapp_message(message_a))
    schedule.every().friday.at("08:00").do(lambda: send_whatsapp_message(message_a))

    # Weekends (Saturday)
    schedule.every().saturday.at("12:00").do(lambda: send_whatsapp_message(message_b))

def run_scheduler():
    print("Scheduler is running...")
    while True:
        schedule.run_pending()  # Check if any scheduled tasks are due
        time.sleep(1)  # Sleep to reduce CPU usage

# Keep-alive function
def keep_alive():
    print("Keep-alive function is running...")
    threading.Thread(target=run_web_server).start()

# Run both Flask and scheduler in parallel
if __name__ == '__main__':
    print("Bot is starting...")
    keep_alive()  # Start the keep-alive server
    run_scheduler()
