FROM python:3.9-slim
WORKDIR /app
COPY api.py api.py
COPY requirements.txt requirements.txt
RUN pip install --upgrade google-cloud-firestore
RUN pip install flask
RUN pip install -U flask-cors
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]