import time
from __main__ import main
from flask import Flask, make_response, jsonify

from common import response, error
from main import app


@app.route("/get/tests/<product>")
def get_tests(product):
    time.sleep(0.25)
    try:
        return response(open(f"api/{product}/tests.json").read())
    except FileNotFoundError:
        return error(f'Tests for product «{product}» were not found', 404)
