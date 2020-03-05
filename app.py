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

@app.route('/getConstituency')
def get_constituency_names():
    res = db.get_constituency_names()
    return jsonify({"names":res})

@app.route('/candidateforconstitu/<constname>')
def candidates_for_constituency(constname):
    res = db.candidates_for_constituency(constname)
    return jsonify({"names":res})

if __name__ == "__main__":
    app.run()