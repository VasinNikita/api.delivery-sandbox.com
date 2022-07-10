import json

from bson import json_util
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/yandex"
mongo = PyMongo(app)
db = mongo.db.yandex

from api.sdd import routes
from api.ndd import routes
from api.gett import routes
from replica.sdd import routes
from handlers import request
from sandbox import routes
from sandbox import user
from sandbox.test import save


def parse_json(data):
    return json.loads(json_util.dumps(data))


@app.route('/mongo')
def mongo():
    collection = db.test
    data = {"name": "Никита"}
    id = collection.insert_one(data).inserted_id

    testData = list(collection.find({}))
    return f"{parse_json(testData)}"


@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({'code': e.code, 'comment': 'Page not found'}), e.code)
