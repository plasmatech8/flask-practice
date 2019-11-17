from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/json")
def hello_json():
    return jsonify({"about": "Hello World!"})

if __name__ == '__main__':
    app.run(debug=True)