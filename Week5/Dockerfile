FROM agrigorev/zoomcamp-model:3.8.12-slim

EXPOSE 5000

# start to install backend-end stuff
RUN mkdir -p /app
WORKDIR /app

# Install Python requirements.
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pip install pipenv
RUN pipenv install --deploy --system

# Copy Script
COPY ["Q5_server.py", "./"]

# Start server
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "Q5_server:app"]
