from flask import Flask, url_for, request, json
import logging
import sys
from timer import countDown as countDown


logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/')
def api_pitimer():
    return 'Hello World'

@app.route('/timer', methods = ['POST'])
def api_timer():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('HEllo')
    logging.info('Data=' + request.data)
    logging.info(request.json["minutes"])
    countDown(int(request.json["minutes"])) 


    return 'List of articles'

if __name__ == '__main__':
    pitimer = logging.getLogger("flask.app")
    pitimer.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    pitimer.addHandler(ch)
    #logging.basicConfig(stream=sys.stdout)
    app.run()