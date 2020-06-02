# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/echo/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    msg = request.args.get("mag", None)

    # For debugging
    print(f"got mag {msg}")

    response = {}

    # Check if user sent a name at all
    if not msg:
        response["ERROR"] = "no message to echo"
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"{msg}"

    # Return the response in json format
    return jsonify(response)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Greetings Earth</h1>"