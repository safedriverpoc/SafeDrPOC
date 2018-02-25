import json
from logging import StreamHandler, DEBUG, Formatter, FileHandler, getLogger

from flask import Flask, jsonify, request

import trainNew
from trainNew import get_prediction, set_prediction
logger = getLogger(__name__)
DIR = 'result_tmp/'
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/addMachine",methods=['POST'])
def addMachine():
    try:
        json_data = request.json['info']
        logger.info('start123')
        logger.info(json_data)
        df = set_prediction(json_data)
        resp_obj = {}
        resp_obj['val'] = [df]
        return jsonify(status='OK',message=str(df))

    except Exception as e:
        logger.info(e);
        return jsonify(status='ERROR',message=str(e))




if __name__ == '__main__':
    log_fmt = Formatter('%(asctime)s %(name)s %(lineno)d [%(levelname)s][%(funcName)s] %(message)s ')
    handler = StreamHandler()
    handler.setLevel('INFO')
    handler.setFormatter(log_fmt)
    logger.addHandler(handler)

    handler = FileHandler(DIR + 'train.py.log', 'a')
    handler.setLevel(DEBUG)
    handler.setFormatter(log_fmt)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.info('start')
    app.run(debug=True)
