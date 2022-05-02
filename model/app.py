import sys
sys.path.insert(1, './predict')

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from prediction import predict

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results',methods=['POST'])
def results():

    features = [x for x in request.form.values()]
    output = predict (features)

    return render_template('index.html', prediction_text='Price should be € {}'.format(output))

#@app.route('/results',methods=['POST'])
#def results():

#    data = request.get_json(force=True)
#    prediction = model.predict([np.array(list(data.values()))])

#    output = prediction[0]
#    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)