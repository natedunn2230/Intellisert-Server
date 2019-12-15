from app import app
from app import light_controller

@app.route('/')
def home():
    return "welcome to basic server. Type 192.168.0.21:5000/light<action> (on, off) to control light"

@app.route('/light/<action>')
def increase_flicker(action):
   if action == 'on':
       light_controller.turn_on()
       return "light activated"
   elif action == 'off':
       light_controller.turn_off()
       return "light de-activated"
   else:
       return 'unknown command \"' + action +  '\"'
