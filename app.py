import numpy as numpy
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    'For rendering resultis in HTML GUI'
    new_review = [str(x) for x in request.form.values()]
    prediction = model.predict(new_review)[0]
    output = prediction
    return render_template('index.html', prediction_text = 'The customer was {}'.format(output))

if __name__ == "__main__":
   app.run(debug=True)