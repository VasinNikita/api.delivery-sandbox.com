import json
import time
from __main__ import main

import requests
from flask import Flask, make_response, jsonify, request

from common import response, error
from main import app, db


@app.route('/test/save', methods=['POST'])
def test_save():
    if 'Authorization' not in request.headers:
        return error("No Authorization header passed", 401)

    token = request.headers['Authorization']
    collection = db.users

    user = collection.find_one({
        "token": token
    })

    collection = db.tests
    collection.update_one({"id": request.json['id'], "step": request.json['step']}, {
        '$set': request.json
    }, upsert=True)
    steps_count = collection.count_documents({"id": request.json['id']})
    collection.update_one({"id": request.json['id'], "step": 0}, {
        '$set': {
            "steps_count": steps_count
        }
    }, upsert=False)

    if not user:
        return error("No user with associated token found", 401)

    return response({"success": 1})
