import json
import time
from __main__ import main

import requests
from flask import Flask, make_response, jsonify, request

from common import response, error, parse_json
from main import app, db


@app.route('/test/get', methods=['GET'])
def test_get():
    if 'Authorization' not in request.headers:
        return error("No Authorization header passed", 401)

    token = request.headers['Authorization']
    collection = db.users

    user = collection.find_one({
        "token": token
    })

    collection = db.tests
    test = db.tests.find_one({"id": request.args.get('id'), "step": int(request.args.get('step'))})

    if not user:
        return error("No user with associated token found", 401)

    if test:
        return response(parse_json(test))
    else:
        return error("No test found with this id and step number")
