import os
import numpy as np 
import matplotlib.pyplot as plt 
from flask import Flask, render_template 

# Flask constructor  
app = Flask(__name__) 

# Generate a scatter plot and returns the Figure and Axes objects
def get_plot(): 
    fig, ax = plt.subplots()
    
    data = { 
        'a': np.arange(50), 
        'c': np.random.randint(0, 50, 50), 
        'd': np.random.randn(50) 
    } 
    data['b'] = data['a'] + 10 * np.random.randn(50) 
    data['d'] = np.abs(data['d']) * 100
    
    ax.scatter(data['a'], data['b'], c=data['c'], s=data['d'])
    ax.set_xlabel('X label') 
    ax.set_ylabel('Y label') 
    
    return fig

# Root URL 
@app.route('/') 
def single_converter(): 
    # Get the matplotlib plot  
    plot = get_plot() 
    
    # Save the figure in the static directory  
    plot.savefig(os.path.join('static', 'images', 'plot.png')) 
    
    # Clear the plot to avoid memory issues
    plt.close(plot)
    
    return render_template('index.html') 

# Main Driver Function  
if __name__ == '__main__': 
    # Run the application on the local development server  
    app.run(debug=True)