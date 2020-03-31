from app import app
from app import light_controller

from flask import jsonify
from flask import request

# HOME ROUTE
@app.route('/')
def home():
    return jsonify({"msg": "Welcome to Intellisert!"}), 200


# LIGHT ROUTES
@app.route('/light/power', methods=["POST"])
def light():
    '''
        Accepts boolean 'power' and dispatches the light controller
        to either turn the light on or off
    '''
    if request.is_json:

        data = request.get_json()

        print(f"Recieved {data}")
        try:
            power = data["power"]
            ## Do light controller stuff

            if power == "on":
                light_controller.turn_on()
            elif power == "off":
                light_controller.turn_off()
            else:
                raise Exception('invalid value')

            return jsonify({"msg": "success"}), 200
        
        except Exception as E:
            print(E)
            return jsonify({"msg": "Bad request. Expecting Key 'power' with Value 'on | off'"}), 400
    

    return jsonify({"msg": "Bad request. Expecting application/json content"}), 400
    
