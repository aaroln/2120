# Imports
import requests
import io
from flask import Flask, request, jsonify, Response, render_template
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import plotly.express as px
from matplotlib.figure import Figure

app = Flask(__name__)

# Load Datasets
dfPop = pd.read_csv('population.csv')
dfLandCover = pd.read_csv('landCover.csv')
dfUrbanLand = pd.read_csv('urbanLand.csv')
dfUrbanPop = pd.read_csv('urbanPop.csv')

@app.route("/")
def countryPop():
    query = request.json.get("query")
    
@app.route('/plotPop.png')
def plot_pngPop():
    fig = create_figure()


def create_figure():
    fig = Figure()
    axis   
    
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()

