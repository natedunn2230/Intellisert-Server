from app import app
from app.light_controller import Controller

from flask import jsonify
from flask import request

# light controller
controller = Controller()

# HOME ROUTE
@app.route('/')
def home():
    return jsonify({"msg": "Welcome to Intellisert!"}), 200


# LIGHT ROUTES
@app.route('/light-state', methods=["GET"])
def light_state():
    '''
        Returns the state of the light, such as if it is
        on or not
    '''
    state = controller.get_state()
    return jsonify(state), 200

@app.route('/light/power', methods=["POST"])
def light_power():
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
                controller.turn_on()
            elif power == "off":
                controller.turn_off()
            else:
                raise Exception('invalid value')

            return jsonify({"power": power}), 200
        
        except Exception as E:
            print(E)
            return jsonify({"power": "Bad request. Expecting Key 'power' with Value 'on | off'"}), 400
    

    return jsonify({"power": "Bad request. Expecting application/json content"}), 400
