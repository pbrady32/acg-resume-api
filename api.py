# TODO
# Set env variable for GCloud Service Account for this session to:
# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\pgbrady\OneDrive - Michigan Medicine\Documents\Desktop\Cloud Computing\Google Cloud\resume_challenge_api\firestore.json"

from google.cloud import firestore
import os
import flask

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.

db = firestore.Client(project='ihpi-testing')


@app.route('/', methods=['GET'])
def home():
    return "<h1>API Home</h1>"


# The Firestore we are using is: db.collection(u'visitors').document(u'visitcount')
doc_ref = db.collection(u'visitors').document(u'visitcount')


@app.route('/count', methods=['GET'])
def get_count():
    doc_data = doc_ref.get().to_dict()

    return int(doc_data['count'])


@app.route('/add', methods=['GET'])
def add_one():
    # Set the count field
    doc_cur_data = doc_ref.get().to_dict()
    doc_ref.update({u'count': int(doc_cur_data['count'])+1})

    # Call again to get updated value
    doc_new_data = doc_ref.get().to_dict()
    return f"<h1>The current count is {doc_new_data['count']} as of today"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))


# def set_count():
#     doc_ref = db.collection(u'visitors').document(u'visitcount')
#     doc_ref.set({
#         u'count': 0
#     })
#     print("set the count")


# set_count()
