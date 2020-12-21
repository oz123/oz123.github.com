import math

from datetime import datetime
from calendar import timegm
from bottle import (Bottle, HTTPResponse, run, request, response,
                    json_dumps as dumps)


FUNCTIONS = {'series A': math.sin, 'series B': math.cos}

app = Bottle()


def convert_to_time_ms(timestamp):
    return 1000 * timegm(
            datetime.strptime(
                timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())


def create_data_points(function, start, end, length=1020):
    lower = convert_to_time_ms(start)
    upper = convert_to_time_ms(end)
    return [[function(i), int(i)] for i in [
        lower + x*(upper-lower)/length for x in range(length)]]


@app.hook('after_request')
def enable_cors():
    print("after_request hook")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = \
        'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route("/", method=['GET', 'OPTIONS'])
def index():
    return "OK"


@app.post('/search')
def search():
    return HTTPResponse(body=dumps(['series A', 'series B']),
                        headers={'Content-Type': 'application/json'})


@app.post('/query')
def query():
    print(request.json)
    if request.json['targets'][0]['type'] == 'table':
        series = request.json['targets'][0]['target']
        bodies = {'series A': [{
            "columns": [
                {"text": "Time", "type": "time"},
                {"text": "Country", " type": "string"},
                {"text": "Number", "type": "number"}
            ],
            "rows": [
                [1234567, "SE", 123],
                [1234567, "DE", 231],
                [1234567, "US", 321]
            ],
            "type": "table"
            }],
            'series B': [{"columns": [
                {"text": "Time", "type": "time"},
                {"text": "Country", "type": "string"},
                {"text": "Number", "type": "number"}
                ],
                "rows": [
                [1234567, "BE", 123],
                [1234567, "GE", 231],
                [1234567, "PS", 321]
            ],
                "type": "table"
            }]}

        series = request.json['targets'][0]['target']
        body = dumps(bodies[series])
    else:
        body = []
        start, end = request.json['range']['from'], request.json['range']['to']
        for target in request.json['targets']:
            name = target['target']
            datapoints = create_data_points(FUNCTIONS[name], start, end)
            body.append({'target': name, 'datapoints': datapoints})

        body = dumps(body)

    return HTTPResponse(body=body,
                        headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    run(app=app, host='localhost', port=8081)
