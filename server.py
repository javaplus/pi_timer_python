from __future__ import print_function
from flask import Flask, url_for, request, json
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Hello World'

@app.route('/timer', methods = ['POST'])
def api_timer():
    logging.basicConfig(level=logging.DEBUG)
    print('HEllo',file=sys.stderr)
    print('Data=' + request.data, file=sys.stderr)
    print(request.json["minutes"], file=sys.stderr)

    return 'List of articles'

if __name__ == '__main__':
    app.run()