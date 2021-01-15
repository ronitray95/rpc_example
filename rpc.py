#!/usr/bin/env python3

import requests


SERVER_URL = 'http://127.0.0.1:5000'
CODES = {200: 'Success', 400: 'Bad request',
         401: 'Unauthorized', 503: 'Service unavailable', 500: 'Server error'}


def init():
    methods = ''
    try:
        r = requests.get(SERVER_URL)
        methods = r.content.decode('utf-8')
    except Exception:
        return 'Unable to contact server', CODES[503]
    for line in methods.split('\n'):
        arr = line.split(' ')
        params = ''
        for i in range(len(arr)):
            if i == 0:
                continue
            params = f'{params}{arr[i]}=x{[i-1]}&'
        postObj = {}
        postObj
        exec(f'''def {arr[0]}(*x): 
                    i=0
                    post={{}}
                    for a in {arr}[1:]:
                        #print(a)
                        post[a]=x[i]
                        i=i+1
                    
                    #print('In RPC',post)
                    r=requests.get('{SERVER_URL}/{arr[0]}',post)
                    return r.content.decode('utf-8'), CODES[r.status_code] ''', globals())
