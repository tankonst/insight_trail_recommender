from flask import Flask
app = Flask(__name__)
app.secret_key = 'the random string'
from app import views
