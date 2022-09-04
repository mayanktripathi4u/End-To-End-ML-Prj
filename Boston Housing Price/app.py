from distutils.log import debug
from operator import methodcaller
import pickle
import os
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
## Load the Model
model = pickle.load(open('boston_house_model.pkl', 'rb'))
sc = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = sc.transform(np.array(list(data.values())).reshape(1,-1))
    pred = model.predict(new_data)
    print(pred[0])

    return jsonify(pred[0])

if __name__ == "__main__":
    app.run(debug = True)



