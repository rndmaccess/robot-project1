import math
from queue import Queue
from flask import Flask, request, jsonify
from flask_cors import CORS
from robot import Robot
import threading

message_queue = Queue()
server_name = "10.130.187.65"

app = Flask(__name__)
CORS(app)


@app.post('/pan_head')
def pan_head():
    if request.is_json:
        data = request.get_json()
        rot = data.get('rot')
        robot = Robot()
        robot.pan_head(rot)
        robot.close()

        return jsonify({"response": f"Received: {data.get('rot', 'no message')}"}), 200
    return jsonify({"error": "Request must be JSON"}), 400


@app.post('/tilt_head')
def tilt_head():
    if request.is_json:
        data = request.get_json()
        rot = data.get('rot')
        robot = Robot()
        robot.tilt_head(rot)
        robot.close()

        return jsonify({"response": f"Received: {data.get('rot', 'no message')}"}), 200
    return jsonify({"error": "Request must be JSON"}), 400



@app.post('/rotate_waist')
def rotate_waist():
    robot = Robot()
    #robot.rotate_waist()
    pass


@app.post('/drive')
def drive():
    if request.is_json:
        data = request.get_json()
        x = data.get('x')
        y = data.get('y')
        steering, throttle = calc_servo_speeds(x, y)

        robot = Robot()
        robot.drive_wheels(int(throttle))
        robot.turn_wheels(int(steering))
        robot.close()


        return jsonify({"response": f"Received: {data.get('x', 'no message'), data.get('y', 'no message')}"}), 200
    return jsonify({"error": "Request must be JSON"}), 400

def calc_servo_speeds(joystick_x, joystick_y):
    angle = math.atan2(joystick_y, joystick_x)
    force_magnitude = math.sqrt((joystick_x ** 2) + (joystick_y ** 2))

    # Normalize the values
    x_norm = math.cos(angle) * force_magnitude
    y_norm = math.sin(angle) * force_magnitude

    # Map these to the maestro controller units (quarter-microseconds)
    x = round(x_norm * 2000 + 6000)
    y = round(y_norm * 2000 + 6000)

    # Constrain the values between 4000 and 8000
    x = max(4000, min(8000, x))
    y = max(4000, min(8000, y))

    steering = x
    throttle = y

    return steering, throttle


@app.post('/speak')
def speak():
    if request.is_json:
        data = request.get_json()
        message = data.get('message')
        message_queue.put(message)
        print(message)

        return jsonify({"response": f"Received: {data.get('message', 'no message')}"}), 200
    return jsonify({"error": "Request must be JSON"}), 400

@app.get('/')
def index():
    return 'Hello World!'

def speak_messages():
    global message_queue
    robot = Robot()

    while True:
        if message_queue.qsize() > 0:
            message = message_queue.get()
            robot.speak(message)


def main():
    thread = threading.Thread(target=speak_messages)
    thread.start()
    robot = Robot()
    robot.drive_wheels(6000)
    app.config["SERVER_NAME"] = server_name
    app.run(host=server_name, port=5002, debug=True)


if __name__ == '__main__':
    main()
