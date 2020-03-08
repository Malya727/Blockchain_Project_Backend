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
    res,name = db.get_candidate_details(voterid)
    return jsonify({"name":name,"details":res})

@app.route('/getConstituency')
def get_constituency_names():
    res = db.get_constituency_names()
    return jsonify({"names":res})

@app.route('/candidateforconstitu/<constname>')
def candidates_for_constituency(constname):
    res = db.candidates_for_constituency(constname)
    return jsonify({"names":res})

@app.route('/UpdateAnalytics/<voterid>')
def update_vote_analytics(voterid):
    res = db.update_vote_analytics(voterid)
    return "<h1>Updated Successfully!</h1>"

@app.route('/GenderwiseCountforConst/<constName>')
def get_voters_gender_count(constName):
    res = db.get_voter_gender_details(constName)
    return jsonify({"gender":res})

@app.route('/VotedGenderwiseCountforConst/<constName>')
def get_voted_gender_details(constName):
    res = db.get_voted_gender_details(constName)
    return jsonify({"gender":res})

@app.route('/totalGenderwiseCount')
def get_voter_gender_details():
    res = db.get_voter_gender_details_total()
    return jsonify({"gender":res})

@app.route('/VotedGenderWiseCountforOverall')
def get_voted_gender_details_overall():
    res = db.get_voted_gender_details_overall()
    return jsonify({"result":res})


if __name__ == "__main__":
    app.run()