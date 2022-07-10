from __main__ import main
from flask import Flask, make_response, jsonify

from main import app

base = "/sdd/webhooks"


@app.route(f"{base}/create")
def webhook_create():
    return make_response(jsonify({'code': 403, 'comment': 'This method is unavailable for sandbox testing. Please use our production environment'}), 403)