from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

print("Hello World!")
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index21.html")

@app.route("/main21", methods=["GET", "POST"])
def main21():
    return render_template("main21.html")

@app.route("/livepolll", methods=["GET", "POST"])
def livepolll():
    return render_template("livepolll.html")

@app.route("/quiz21", methods=["GET", "POST"])
def quiz21():
    return render_template("quiz21.html")

if __name__ == "__main__":
    app.run(debug=True)
