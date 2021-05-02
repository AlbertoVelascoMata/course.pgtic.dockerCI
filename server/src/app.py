#!/usr/bin/python3

from flask import Flask, Blueprint
from flask import request, jsonify
from flask import current_app

bp = Blueprint('sensors', __name__)

@bp.route("/sensors", methods=('GET', 'POST'))
def test():
    if request.method == 'POST':
        # POST: register new sensor
        name = request.args.get('name', 'Unknown')
        version = request.args.get('version', '1.0')
        id = str(len(current_app.config['sensors']))
        current_app.config['sensors'][id] = {
            'name': name,
            'version': version
        }
        return jsonify(current_app.config['sensors'][id])

    else:
        # GET: obtain list of registered sensors
        return jsonify(current_app.config['sensors'])

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)

    # Simulate database
    app.config['sensors'] = {}

    return app
