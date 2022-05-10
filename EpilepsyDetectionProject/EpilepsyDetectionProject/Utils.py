import csv
import json
import pandas as pd


def convertCSVtoJSON():
    csvfilePath = 'venv/input/PatientData.csv'
    jsonfilePath = 'venv/input/PatientData.json'
    df = pd.read_csv(csvfilePath)
    df.to_json(jsonfilePath)


def convertJSONoCSV():
    csvfilePath = 'venv/input/PatientDataConverted.csv'
    jsonfilePath = 'venv/input/GoodPatientData.json'
    df = pd.read_json(jsonfilePath)
    df.to_csv(csvfilePath, index=False)


def convertJSONoCSV(jsonObject):
    csvfilePath = 'venv/input/APICustomerData.csv'
    jsonfilePath = 'venv/input/APICustomerData.json'
    df = pd.read_json(jsonfilePath)
    df.to_csv(csvfilePath, index=False)
    return csvfilePath;


def writeJsonToFile(jsonObject):

    with open('venv/input/APICustomerData.json', 'w') as outfile:
        json.dump(jsonObject, outfile)
