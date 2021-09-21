FROM python:3.9-slim-buster
WORKDIR /app
COPY api.py api.py
COPY requirements.txt requirements.txt
COPY firestore.json firestore.json
RUN pip install --upgrade google-cloud-firestore
RUN pip install flask
ENV GOOGLE_APPLICATION_CREDENTIALS=firestore.json
# ENTRYPOINT ["python"]
CMD python api.py