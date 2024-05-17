from flask import Flask, request, jsonify
from aiogram import Bot, Dispatcher, types
import asyncio


app = Flask(__name__, static_folder='frontend/dist', static_url_path='')
bot = Bot(token='5519529925:AAFGWXUQpQ-BfYdkWZMG1hGyNmEWI1tjZnY')
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
ADMIN_ID = 1228378766

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/studrada', methods=['GET'])
def get_studrada():
    return app.send_static_file('studrada.html')

@app.route('/studrada', methods=['POST'])
def send_studrada():
    # print(request.form)
    name = request.form['name']
    group = request.form['group']
    contact = request.form['contact']
    text = request.form['text']
    loop.run_until_complete(bot.send_message(ADMIN_ID, f'Ім я: {name}\nГрупа: {group}\nКонтакт: {contact}\nТекст: {text}'))
    return app.send_static_file('studrada.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

app.run()