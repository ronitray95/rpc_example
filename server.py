#!/usr/bin/env python3


from flask import *
import math
app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Hello World', 200


@app.route('/power')
def service1():
    if request.method == 'POST':
        return 'Not supported', 401
    x = request.args.get('x')
    y = request.args.get('y')
    if x is None or y is None:
        return 'One or more parameters is absent', 400
    try:
        x = int(x)
        y = int(y)
        return str(x ** y), 200
    except Exception:
        return 'Bad integer format', 400


@app.route('/sqrt')
def service2():
    if request.method == 'POST':
        return 'Not supported', 401
    x = request.args.get('x')
    if x is None:
        return 'Parameter is absent', 400
    try:
        return str(math.sqrt(x)), 200
    except Exception:
        return 'Bad number format', 400


if __name__ == '__main__':
    app.run(debug=True)
