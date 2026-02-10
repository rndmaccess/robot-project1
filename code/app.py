from flask import Flask, request, jsonify
from flask_cors import CORS
from robot import Robot



server_name = "therobot.localhost"

app = Flask(__name__)
CORS(app)


@app.post('/pan_head')
def pan_head():
    if request.is_json:
        data = request.get_json()
        robot = Robot()
        #robot.pan_head()

        print("Recieved data: " + data)

        return jsonify({"message": "Data recieved successfully",  "yourData": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@app.post('/tilt_head')
def tilt_head():
    robot = Robot()
    #robot.tilt_head()
    pass


@app.post('/rotate_waist')
def rotate_waist():
    robot = Robot()
    #robot.rotate_waist()
    pass


# Currently this is the only method that is attached to the joystick!
@app.post('/drive')
def drive():
    if request.is_json:
        data = request.get_json()
        x = data.get('x')
        y = data.get('y')
        print("Data received:", x, y)
        normalized_x = normalize_joystick(x)
        normalized_y = normalize_joystick(y)
        robot = Robot()
        # robot.drive_wheels()

        return jsonify({"response": f"Received: {data.get('message', 'No message')}"})
    return None

# This method normalizes the positions that
# come back from our joystick!
def normalize_joystick(pos):
    center_point = 30
    normalized_pos = (pos - center_point) / center_point
    # A small deadzone for minor fluctuations
    if abs(normalized_pos) < 0.1:
        return 0
    return normalized_pos

@app.get('/')
def index():
    return 'Hello World!'


def main():
    app.config["SERVER_NAME"] = server_name 
    app.run(host=server_name, port=5002, debug=True)


if __name__ == '__main__':
    main()
