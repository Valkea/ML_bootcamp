FROM agrigorev/zoomcamp-cats-dogs-lambda:v2

# install Python requirements
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pip install pipenv
run pipenv install --deploy --system 

# Same as:
#RUN pip install numpy
#RUN pip install pillow
## TF-Lite for Devian / Ubuntu
# RUN pip install --extra-index-url https://google-coral.github.io/py-repo/ tflite-runtime
## TF-Lite for Amazon Linux (CentOS)
#RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl?raw=true

# Copy Script
COPY tflite_model.py .

CMD ["tflite_model.lambda_handler"] 
# docker run -it --rm -p 8080:8080 dogs-cats:latest
