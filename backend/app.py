from flask import Flask, jsonify, request
from flask_cors import CORS

 
# configuration
DEBUG = True
 
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
 
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def main():
    return 'This is Main ROUTE!'

@app.route('/submit', methods=['POST'])
def submit_answers():
    depression_scale = {
        "not-at-all": 0,
        "several-days": 1,
        "more-than-half": 2,
        "nearly-every-day": 3
    }

    
    data = request.json  # Get JSON data from the request

    # Initialize the score
    score = 0

    # Iterate through each question and calculate the score
    for key, value in data.items():
        score += depression_scale.get(value, 0)

    # Determine the severity based on the score
    if 0 <= score <= 4:
        severity = "No depression"
    elif 5 <= score <= 9:
        severity = "Mild depression"
    elif 10 <= score <= 14:
        severity = "Moderate depression"
    elif 15 <= score <= 19:
        severity = "Moderately severe depression"
    elif 20 <= score <= 27:
        severity = "Severe depression"
    else:
        severity = "Invalid score" 

    # Return the result as JSON
    return jsonify({"score": score, "severity": severity})

  
 
if __name__ == '__main__':
    app.run(port=3001) 