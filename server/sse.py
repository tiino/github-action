import bottle
from bottle import run, route, response, request
import time


@route('/sse')
def sse_request():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content_Type']  = 'text/event-stream'

    for i in range(100):
        yield "event: clock\n".encode("utf-8")
        yield f'data: {{"time": "{time.time()}", "c": {i} }}\n'.encode("utf-8")
        yield "\n".encode("utf-8")

        time.sleep(0.5)


@route('/sse', method='POST')
def sse_post():
    val = [val for val in request.body][0]

    return bottle.HTTPResponse(status=200, body=val)


if __name__ == '__main__':
    run(host="localhost", port=8787, debug=True, reloader=True)
