from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit

app = Flask(__name__) # Updated
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smart_classroom.db"
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
class Class(db.Model):
    roll_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
class Student(db.Model):
    roll_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    class_ = db.relationship("Class", backref="students")

class Quiz(db.Model):
    roll_no = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100), nullable=False)
    option4 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
class Poll(db.Model):
    roll_no = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100), nullable=False)

@app.before_request # Updated
def create_tables():
    db.create_all()
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        roll_no = data.get("enrollment_no")
        password = data.get("password")
        name = data.get("name")
        # Validate login credentials (this is just a placeholder)
        return jsonify({"success": True, "message": "Logged in successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/students", methods=["GET"]) 
def get_students():
    try:
        students = Student.query.all()
        student_list = [{"roll_no.": student.roll_no, "name": student.name} for student in students]
        return jsonify({"students": student_list})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
@app.route("/add_student", methods=["POST"])
def add_student():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        # Add new student (this is just a placeholder, you should add to the database)
        new_student = Student(name=name)
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"success": True, "message": "Student added successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
@app.route("/polls", methods=["GET"])
def get_polls():
    try:
        polls = Poll.query.all()
        poll_list = [{"roll_no.": poll.roll_no, "question": poll.question, "option1": poll.option1, "option2": poll.option2, "option3": poll.option3} for poll in polls]
        return jsonify({"polls": poll_list})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
@app.route("/submit_poll", methods=["POST"])
def submit_poll():
    try:
        data = request.json
        poll_id = data.get("poll_id")
        answer = data.get("answer")
        # Update poll results (this is just a placeholder)
        return jsonify({"success": True, "message": "Poll submitted successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
@socketio.on("connect")
def connect():
    print("Client connected")
@socketio.on("disconnect")
def disconnect():
    print("Client disconnected")
@socketio.on("quiz_submission")
def handle_quiz_submission(data):
    try:
        # Handle quiz submission (this is just a placeholder)
        results = {"quiz_id": data.get("quiz_id"), "status": "processed"}
        emit("quiz_results", results)
    except Exception as e:
        emit("quiz_results", {"error": str(e)})
@socketio.on("poll_submission")
def handle_poll_submission(data):
    try:
        # Handle poll submission (this is just a placeholder)
        results = {"poll_id": data.get("poll_id"), "status": "processed"}
        emit("poll_results", results)
    except Exception as e:
        emit("poll_results", {"error": str(e)})
if __name__ == "main": # Updated
    socketio.run(app, debug=True)
