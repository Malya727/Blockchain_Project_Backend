from flask import Flask,jsonify
from mongo_flask import MongoJSONEncoder
from flask_cors import CORS,cross_origin
import database as db

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

@app.route('/')
def index():
    return "<h1>Hey! Boys API is Working Fine</h1>"

@app.route('/getCandidateDetails/<voterid>')
def get_candidate_details(voterid):
    res = db.get_candidate_details(voterid)
    return jsonify({"details":res})

if __name__ == "__main__":
    app.run()