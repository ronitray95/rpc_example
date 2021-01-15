#!/usr/bin/env python3


from flask import *
import math
app = Flask(__name__)


@app.route('/')
def homepage():
    s = 'power x y\nsqrt x'
    return s, 200


@app.route('/power')
def power():
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
    except Exception as e:
        return f'Bad integer format {e}', 400


@app.route('/sqrt')
def sqrt():
    if request.method == 'POST':
        return 'Not supported', 401
    x = request.args.get('x')
    if x is None:
        return 'Parameter is absent', 400
    try:
        return str(math.sqrt(float(x))), 200
    except Exception as e:
        return f'Bad number format {e}', 400


if __name__ == '__main__':
    app.run(debug=True)
