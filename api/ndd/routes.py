from __main__ import main
from flask import Flask, make_response, jsonify

from main import app

# base = "/b2b/cargo/integration"


# @app.route(f"{base}/v2/claims/create.json")
# def claims_create():
#     return make_response(jsonify({'code': 403, 'comment': 'This method is unavailable for sandbox testing. Please use our production environment'}), 403)