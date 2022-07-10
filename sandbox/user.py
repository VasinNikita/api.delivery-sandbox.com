import json
import time
from __main__ import main

import requests
from flask import Flask, make_response, jsonify, request

from common import response, error
from main import app, db


@app.route('/user/create', methods=['POST'])
def user_create():
    token = request.json['token']

    url = "https://login.yandex.ru/info"
    querystring = {"oauth_token": token}

    r = requests.request("GET", url, data="", headers={}, params=querystring)
    j = json.loads(r.text)

    data = {"token": token, "avatar": f'https://avatars.mds.yandex.net/get-yapic/{j["default_avatar_id"]}/islands-68', "name": j['real_name'], "has_plus": False, "yandex_id": j['id']}
    collection = db.users
    id = collection.update_one({
        'yandex_id': j['id']
    }, {
        '$set': data
    }, upsert=True).upserted_id

    return response({"userpic": data['avatar'], 'id': id if id is not None else str(collection.find_one({"yandex_id": j['id']})['_id'])})


@app.route("/user/progress")
def user_progress():
    time.sleep(0.5)
    return response({
        "express": {
            "current": 15,
            "max": 35
        },
        "sdd": {
            "current": 500,
            "max": 600
        },
        "ndd": {
            "current": 50,
            "max": 100
        }
    })
