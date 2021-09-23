from google.cloud import firestore
import os
import flask
from flask import jsonify
from flask_cors import CORS


app = flask.Flask(__name__)
# app.config["DEBUG"] = True
cors = CORS(app)

db = firestore.Client()


@app.route('/', methods=['GET'])
def home():
    return "<h1>This is the home of the pgbcloud.com visitor count API.</h1>"


# The Firestore we are using is: db.collection(u'visitors').document(u'visitcount')
doc_ref = db.collection(u'visitors').document(u'visitcount')


# Set up a route to retrieve the current visitor count
@app.route('/count', methods=['GET'])
def get_count():
    doc_data = doc_ref.get().to_dict()
    return jsonify({"count": doc_data['count']})


# Set up a route to increment the current visitor count by 1, and then return the current count
@app.route('/add', methods=['GET'])
def add_one():
    # Set the count field
    doc_cur_data = doc_ref.get().to_dict()
    doc_ref.update({u'count': int(doc_cur_data['count'])+1})

    # Call again to get updated value
    doc_new_data = doc_ref.get().to_dict()
    return f"The current count is {doc_new_data['count']}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
