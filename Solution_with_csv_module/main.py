# coding=utf-8

from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def pets_in_city():
    return 'Flask server test'


if __name__ == '__main__':
    app.run()