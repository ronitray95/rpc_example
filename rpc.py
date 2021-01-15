#!/usr/bin/env python3

import requests


SERVER_URL = 'http://127.0.0.1:5000'
CODES = {200: 'Success', 400: 'Bad request',
         401: 'Unauthorized', 503: 'Service unavailable'}


def testServer():
    try:
        r = requests.get(SERVER_URL)
        return r.content.decode('utf-8'), CODES[r.status_code]
    except Exception:
        return 'Unable to contact server', CODES[503]


def power(x, y):
    try:
        r = requests.get(f'{SERVER_URL}/power?x={x}&y={y}')
        return r.content.decode('utf-8'), CODES[r.status_code]
    except Exception:
        return 'Unable to contact server', CODES[503]


def sqrt(x):
    try:
        r = requests.get(f'{SERVER_URL}/sqrt?x={x}')
        return r.content.decode('utf-8'), CODES[r.status_code]
    except Exception:
        return 'Unable to contact server', CODES[503]
