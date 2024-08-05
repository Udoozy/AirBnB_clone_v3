#!/usr/bin/python3
"""
This is to create variable app instance of Flask
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_handler(exception):
    """
    This is handle error 404
    """
    storage.close()

@app.errorhanlder(404)
def not_found(error):
    """
    This is coustomized error handler
    """
    response = {"error": "Not found"}
    return jsonify(response), 404


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
