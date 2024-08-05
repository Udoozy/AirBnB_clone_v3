#!/usr/bin/python3
"""
this create app_views
"""

from api.vi.views import app_views
from flask import jsonify


@app_views.route('/status')
def ap_status():
    """
    """
    response = {"status": "OK"}
    return jsonify(response)
