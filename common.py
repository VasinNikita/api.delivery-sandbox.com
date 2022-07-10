import time

import requests
from flask import request, Response, make_response, jsonify, json


def proxy(method='POST', current_host='https://b2b.taxi.tst.yandex.net/'):
    if request.method == "POST":
        resp = requests.request(
            method='POST',
            url=request.url.replace(request.host_url, current_host),
            headers={key: value for (key, value) in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False)

        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                   if name.lower() not in excluded_headers]

        response = Response(resp.content, resp.status_code, headers)
        return response
    else:
        return make_response(jsonify({'code': 405, 'comment': f'{request.method} is not allowed'}), 405)


def response(text, code=200):
    try:
        text = json.loads(text)
    except ValueError:
        pass
    except TypeError:
        text = text

    time.sleep(0.1)

    r = make_response(text, code)
    r.headers['Content-Type'] = 'application/json'
    r.headers['Accept-Language'] = 'ru'
    return r


def error(comment, code=400):
    r = make_response(jsonify({"code": code, "comment": comment}), code)
    r.headers['Content-Type'] = 'application/json'
    r.headers['Accept-Language'] = 'ru'
    return r
