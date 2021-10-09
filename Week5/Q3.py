#! /usr/bin/env python3
# coding: utf-8

import pickle

# --- Load DictVectorizer & Model ---

print("Load DictVectorizer & Model")

with open('data/dv.bin', 'rb') as f:
    dv = pickle.load(f)

with open('data/model1.bin', 'rb') as f:
    model = pickle.load(f)

# --- Vectorize test user ---

print("Vectorize test user")

test_customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

X = dv.transform(test_customer)

# --- Predict using the test user ---

print("Predict")

pred = model.predict_proba(X)

print(f"Probability of churning for the test user: {pred[0][1]:.3f}")
