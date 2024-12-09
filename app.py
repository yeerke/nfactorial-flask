from flask import Flask, render_template
from models.student import Student

app = Flask(__name__)

students = [
    Student("Alice Johnson", "Computer Science", "Sophomore"),
    Student("Bob Smith", "Mechanical Engineering", "Senior"),
    Student("Charlie Brown", "Mathematics", "Junior"),
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/students")
def student_list():
    return render_template("student_list.html", students=students)

@app.route("/students/<int:student_id>")
def student_details(student_id):
    student = next((s for s in students if s.id == student_id), None)
    if not student:
        return "Student not found!", 404
    return render_template("student_details.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)