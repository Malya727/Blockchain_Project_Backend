from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb+srv://react:react@malya-gso2y.mongodb.net/test?retryWrites=true&w=majority/")

db = client.Election_Blockchain


def get_candidate_details(voterid):
    collection1 = db.Voter_Details
    constitu = collection1.find({"voter_id": voterid} , {"_id":0,"constituency":1})
    res = [f for f in constitu]
    constituency_name = res[0]['constituency']
    collection2 = db.Candidate_Details
    res = collection2.find({"constituency": constituency_name},{"_id":0})
    return [r for r in res]

def get_constituency_names():
    collection = db.Candidate_Details
    constitu = collection.distinct('constituency')
    return [c for c in constitu]

def candidates_for_constituency(const_name):
    collection2 = db.Candidate_Details
    res = collection2.find({"constituency": const_name},{"_id":0})
    return [r for r in res]

def get_voter_gender_details(constName):
    collection2 = db.Voter_Details
    res = collection2.aggregate([

        {"$match":{"constituency": constName}
        },
        {"$project": {
            "male": {"$cond": [{"$eq": ["$gender", "Male"]}, 1, 0]},
            "female": {"$cond": [{"$eq": ["$gender", "Female"]}, 1, 0]},
        }},
        {"$group": { "_id": "null", "male": {"$sum": "$male"},
                                "female": {"$sum": "$female"},
                                "total": {"$sum": 1},
        }},
        {"$project":{"male":"$male","female":"$female", "total": "$total", "_id":0}}

        ])
    return [r for r in res]