from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='frontend/dist', static_url_path='')

app.run()