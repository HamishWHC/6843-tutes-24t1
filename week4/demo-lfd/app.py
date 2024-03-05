from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/files")
def view_file():
    filename = request.args.get("filename")
    if type(filename) is not str:
        return abort(400, "missing filename parameter")

    return open("./" + filename).read()


if __name__ == "__main__":
    app.run(port=4999, debug=True)
