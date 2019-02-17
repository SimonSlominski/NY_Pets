from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/, methods=['GET'])
def pets_in_city():
    return 'test Flask server'


if __name__ == '__main__':
    app.run()