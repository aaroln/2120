import requests
import pandas

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
dataOS = pd.read_csv('openSpace.csv')

column_name = 'Value'

# Check if the column exists in the DataFrame
if column_name in dataOS.columns:
    # Calculate the average of the specified column
    average_value = dataOS[column_name].mean()
    
    print(f"The average value of '{column_name}' is: {average_value}")
else:
    print(f"Column '{column_name}' not found in the CSV file.")


@app.route('/api/get_value', methods=['POST'])
def get_value():
    query = request.json.get("query")
    country = dataOS[dataOS["GeoAreaName"].str.lower() == query.lower()]
    if not cities.empty:
        countryData = {}
        
        for index, row in country.iterrows():
            city_name = row["Cities"]
            city_value = row["Value"]
            
            # Add the city name and value to the dictionary
            countryData[city_name] = city_value

        result = {
            "Country": query,
            "Cities": countryData,
            "Global Mean": 
        }
        return jsonify(result)
    return jsonify({"ERROR": "Country not found"}), 404
 
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)