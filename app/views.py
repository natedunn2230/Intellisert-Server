from app import app
from app import light_controller

@app.route('/')
def home():
    return "Welcome to Intellisert!"