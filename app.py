from flask import Flask
from robot import Robot


app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.post('/pan_head')
def pan_head():
    robot = Robot()
    robot.pan_head()


@app.post('/tilt_head')
def tilt_head():
    robot = Robot()
    robot.tilt_head()


@app.post('/rotate_waist')
def rotate_waist():
    robot = Robot()
    robot.rotate_waist()


@app.post('/drive')
def drive():
    robot = Robot()
    robot.drive_wheels()


@app.get('/')
def index():
    return 'Hello World!'


def main():
    app.run()


if __name__ == '__main__':
    main()