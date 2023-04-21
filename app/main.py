from flask import Flask,jsonify,request
import json
app = Flask(__name__)


data = [{
    "id":1,
    "notes":"sample notes",
    "completed":"true",
    }]


@app.route("/",methods=['GET'])
def health():
    return jsonify("This is python based test server")

@app.route('/notes',methods = ['GET'])
def get_notes():
    return jsonify(data)

@app.route("/notes",methods=["POST"])
def add_notes():
    record = request.get_json()
    data.append({"id":record["id"],"notes":record["notes"],"completed":record["completed"]})
    return jsonify("data added success")

@app.route("/notes/<note_id>",methods=["GET"])
def get_note_by_id(note_id):
    print(note_id)
    for d in data:
        if d["id"] == int(note_id):
            return jsonify(d)
    return jsonify("no such notes found with id")

if __name__ == '__main__':
    app.run(host="0.0.0.0")

