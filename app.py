# Imports
import requests
from flask import Flask, request, jsonify
import pandas as pd
import matplotlib as plt

app = Flask(__name__)

# Load Dataset
dataPop = pd.read_csv('pop.csv')
dataOs = pd.read_csv('openSpace.csv')

dataPopT = dataPop.transpose()

newfile = 'population.csv'

dataPopT.to_csv(newfile)

'''
@app.route("/")
def countryPop():
    query = request.json.get("query")
    
    
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
'''
