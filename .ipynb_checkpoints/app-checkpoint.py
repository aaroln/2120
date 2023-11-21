# Imports
import requests
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load Dataset
dataPop = pd.read_csv('population.csv')
dataOs = pd.read_csv('openSpace.csv')

@app.route("/")
def countrySearch():
    return ""

if __name__ == "__main__":
    app.run()