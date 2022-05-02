from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


def predict(features):
    
    features = [x for x in request.form.values()]
    int_features = features[0:3]
    int_features = [int(s) for s in int_features]
    status = features[3]

    if (status == '0' or status =='1'):
        model = pickle.load(open('./model/model1.pkl', 'rb'))
    else:
        model = pickle.load(open('./model/model2.pkl', 'rb'))
        
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0])

    return output