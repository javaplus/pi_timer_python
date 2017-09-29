from flask import Flask, request, json
import logging
import sys
import timer
#from timer import stopCountDown

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/')
def api_pitimer():
    return 'Hello World'

@app.route('/stop')
def api_stop():
    timer.stopCountDown()
    return 'stopping'

@app.route('/timer', methods = ['POST'])
def api_timer():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('HEllo')
    logging.info('Data=' + request.data)
    logging.info(request.json["minutes"])
    timer.countDown(int(request.json["minutes"])) 


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
    app.run(host='0.0.0.0')