FROM python:3.9-slim-buster
WORKDIR /app
COPY api.py api.py
COPY requirements.txt requirements.txt
# COPY firestore.json firestore.json
RUN pip install --upgrade google-cloud-firestore
RUN pip install flask
RUN pip install flask-cors
# ENV GOOGLE_APPLICATION_CREDENTIALS=firestore.json
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 api:app
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]