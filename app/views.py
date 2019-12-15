from app import app

@app.route('/')
def home():
    return "welcome to basic server"

@app.route('/increase')
def increase_flicker():
   return "this endpoint will increase light flicker"

@app.route('/decrease')
def decrease_flicker():
  return "this endpoint will decrease light flicker"

