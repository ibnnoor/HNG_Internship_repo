import datetime
from flask import Flask, request, jsonify

date = datetime.datetime.now()
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello"
 

@app.route("/api")
def api():
  data = {
    "current_day": date.strftime("%A"),
    "utc_time": date.strftime("%H:%M:%S"),
    "github_file_url": "",
    "github_repo_url": "https://github.com/ibnnoor/HNG_Internship_repo",
    "status_code": 200
  }

  slack_name = request.args.get("slack_name")
  track = request.args.get("track")
  if slack_name:
    data["slack_name"] = slack_name
  if track:
    data["track"] = track  

  return jsonify(data), 200

if __name__ == "__main__":
  app.run(debug=True)