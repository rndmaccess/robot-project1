from flask import Flask
from robot import Robot


app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.get('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()