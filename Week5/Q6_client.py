#! /usr/bin/env python3
# coding: utf-8

import requests

url = "http://0.0.0.0:5000/predict"
customer = {'contract': 'two_year', 'tenure': 12, 'monthlycharges': 10}

try:
    result = requests.post(url, json=customer).json()
    print(result)
except Exception as error_msg:
    print(f'AN ERROR OCCURED:\n{error_msg}')
