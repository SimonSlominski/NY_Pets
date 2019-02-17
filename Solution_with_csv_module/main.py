from flask import Flask
from flask import jsonify

from search import find_pets

app = Flask(__name__)


@app.route('/api/v1/<city>', methods=['GET'])
def pets_in_city(city):
    return jsonify(find_pets(city))


if __name__ == '__main__':
    app.run()
