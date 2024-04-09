from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/missing-cors.json")
def missing_cors():
    return jsonify({"some": "data"})


@app.route("/wrong-cors.json")
def wrong_cors():
    response = jsonify({"some": "data"})
    response.access_control_allow_origin = "https://quoccabank.com"
    return response


@app.route("/cors.json")
def cors():
    response = jsonify({"some": "data"})
    response.access_control_allow_origin = "http://localhost:8001"
    return response


@app.route("/post.json", methods=["POST", "OPTIONS"])
def post():
    response = jsonify({"some": "data"})
    response.headers.set("Access-Control-Allow-Methods", "POST")
    response.access_control_allow_origin = "http://localhost:8001"
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8002)
