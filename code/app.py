from queue import Queue
from flask import Flask, request, jsonify
from flask_cors import CORS
from robot import Robot
import threading

message_queue = Queue()
server_name = "therobot.localhost"

app = Flask(__name__)
CORS(app)


@app.post('/pan_head')
def pan_head():
    if request.is_json:
        data = request.get_json()
        rot = data.get('rot')
        robot = Robot()
        robot.pan_head(rot)

        return jsonify({"response": f"Received: {data.get('rot', 'no message')}"}), 200
    return jsonify({"error": "Request must be JSON"}), 400


@app.post('/tilt_head')
def tilt_head():
    if request.is_json:
        data = request.get_json()
        rot = data.get('rot')
        robot = Robot()
        robot.tilt_head(rot)

        return jsonify({"response": f"Received: {data.get('rot', 'no message')}"}), 200
    return jsonify({"error": "Request must be JSON"}), 400



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
        left_servo_speed, right_servo_speed = calc_servo_speeds(x, y)
        print(left_servo_speed, ",", right_servo_speed)

        robot = Robot()
        robot.drive_wheels(left_servo_speed)
        robot.drive_wheels(right_servo_speed)

        return jsonify({"response": f"Received: {data.get('x', 'no message'), data.get('y', 'no message')}"}), 200
    return jsonify({"error": "Request must be JSON"}), 400

def calc_servo_speeds(joystick_x, joystick_y):
    # Mix steering and drive
    left_motor = joystick_y + joystick_x
    right_motor = joystick_y - joystick_x

    # Normalize to keep within +/- 30.
    # This prevents steering loss at high speeds!
    max_val = max(abs(left_motor), abs(right_motor))
    if max_val > 30:
        left_motor = (left_motor / max_val) * 30
        right_motor = (right_motor / max_val) * 30

    # Assuming 6000 is center
    left_servo_speed = int(6000 - (left_motor * 66.66))
    right_servo_speed = int(6000 - (right_motor * 66.66))
    return left_servo_speed, right_servo_speed


@app.post('/speak')
def speak():
    if request.is_json:
        data = request.get_json()
        message = data.get('message')
        message_queue.put(message)

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
    thread.join()
    app.config["SERVER_NAME"] = server_name
    app.run(host=server_name, port=5002, debug=True)


if __name__ == '__main__':
    main()
