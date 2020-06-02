# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/echo/", methods=["GET"])
def respond():
    # Get msg from param
    msg = request.args.get("msg", None)

    # For debugging
    print(f"got msg: {msg}")

    response = {}

    # Check for msg
    if not msg:
        response["ERROR"] = "no message to echo"
    else:
        response["ECHO"] = f"{msg}"

    # Return msg in json
    return jsonify(response)


# Base page
@app.route("/")
def index():
    return "<h1>Greetings Earth</h1>"
