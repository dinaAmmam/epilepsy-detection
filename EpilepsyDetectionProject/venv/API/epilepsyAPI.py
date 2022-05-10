from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

import SeizureMatchingUtils
import Utils

app = Flask(__name__)
api = Api(app)

@app.route('/detection', methods=['POST'])
def detectEpilepsy():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        # convert json to csv then pass it to the detection method and return true or false
        Utils.writeJsonToFile(json)
        CSVPatientData =  Utils.convertJSONoCSV(json)
        result = SeizureMatchingUtils.checkPatientData(CSVPatientData)
        if result:

            return '"yes" you might get seizure be conscious about it'
        else:

            return 'You are safe no worries :)'
        return result
    else:
        return 'Content-Type not supported!'