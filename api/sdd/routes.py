import requests as requests
from flask import Flask, make_response, jsonify, request, Response

from common import proxy, response
from main import app

test = True

yandexTestHost = 'https://b2b.taxi.tst.yandex.net/'
yandexProdHost = 'https://b2b.taxi.yandex.net/'
currentHost = yandexTestHost if test else yandexProdHost

base = "/b2b/cargo/integration"


@app.route(f"{base}/v2/claims/create", methods=['POST', 'GET'])
def claims_create():
    response = proxy()
    return response


@app.route(f"{base}/v1/claims/accept", methods=['POST', 'GET'])
def claims_accept():
    response = proxy()
    return response


@app.route(f"{base}/v1/claims/return")
def claims_return():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v1/claims/cancel")
def claims_cancel():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v1/claims/points-eta")
def claims_points_eta():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v1/check-price")
def check_price():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v1/tariffs")
def tariffs():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v1/delivery-methods")
def delivery_methods():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v2/claims/edit")
def claims_edit():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v2/claims/confirmation_code")
def claims_confirmation_code():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v2/claims/bulk_info")
def claims_bulk_info():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v2/claims/info")
def claims_info():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v2/claims/cancel-info")
def claims_cancel_info():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v2/claims/search")
def claims_search():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v2/claims/search/active")
def claims_search_active():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v1/claims/robot/open-request")
def robot_open_request():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v1/claims/robot/check-availability")
def robot_check_availability():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)


@app.route(f"{base}/v1/claims/document")
def claims_document():
    return response(f'{request.path} method is unavailable for sandbox testing. Please use our production environment', 403)
