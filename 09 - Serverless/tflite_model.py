#!/usr/bin/env python
# coding: utf-8

from io import BytesIO
from urllib import request

from PIL import Image
import numpy as np
import tflite_runtime.interpreter as tflite


# --- Load TF-Lite model using an interpreter

interpreter = tflite.Interpreter(model_path="cats-dogs-v2.tflite")

interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]


# --- Load & prepare image


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != "RGB":
        img = img.convert("RGB")
    img = img.resize(target_size, Image.NEAREST)
    return img


# --- Preprocess input
# We can see the preprocessing steps used in the TF model here:
# https://github.com/Valkea/ML_bootcamp/blob/main/08%20-%20Deep%20Learning.ipynb
# https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/08-deep-learning/CNN_solution.ipynb


def preprocess_input(X):
    X_pre = X / 255.0  # As defined in the dog & cat TF CNN
    return X_pre


def predict(url):

    # Load & prepare image
    img = download_image(url)
    img = prepare_image(img, (150, 150))

    x = np.array(img, dtype=np.float32)
    X = np.array([x])

    # Preprocess input
    X_pre = preprocess_input(X)

    # Apply model
    interpreter.set_tensor(input_index, X_pre)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    return preds[0].tolist()


# --- AWS Lambda handler

def lambda_handler(event, context):
    url = event['url']
    return predict(url)


# ref_url = "https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg"
# print(predict(ref_url))
