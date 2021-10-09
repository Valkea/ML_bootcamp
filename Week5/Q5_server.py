#! /usr/bin/env python3
# coding: utf-8

import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)


# --- Load DictVectorizer & Model ---

print("Load DictVectorizer & Model")
with open('dv.bin', 'rb') as f:
    dv = pickle.load(f)

with open('model2.bin', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return f"Hello world !"


@app.route('/predict', methods=['POST'])
def predict():
    user_infos = request.get_json()

    X = dv.transform(user_infos)
    pred = model.predict_proba(X)
    return jsonify(f"Probability of churning for this user: {pred[0][1]}")


print("Server ready")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
