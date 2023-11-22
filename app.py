# Imports
import requests
from flask import Flask, request, jsonify
import pandas as pd
import matplotlib as plt

app = Flask(__name__)

# Load Dataset
dfPop = pd.read_csv('population.csv')
dfLandCover = pd.read_csv('landCover.csv')
dfUrbanLand = pd.read_csv('urbanLand.csv')
dfUrbanPop = pd.read_csv('urbanPop.csv')


# Define the value you want to filter on
desired_value = 'Artificial surfaces'

# Filter rows based on the condition
filtered_df = dfLandCover[dfLandCover['Land cover class'] == desired_value]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_file.csv', index=False)

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
