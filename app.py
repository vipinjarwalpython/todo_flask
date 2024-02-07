from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.tittle}"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tittle = request.form["tittle"]
        desc = request.form["desc"]

        todo = Todo(tittle=tittle, desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template("index.html", alltodo=alltodo)


@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    if request.method == "POST":
        tittle = request.form["tittle"]
        desc = request.form["desc"]

        todo = Todo.query.filter_by(sno=sno).first()
        todo.tittle = tittle
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo)


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    print(todo)
    db.session.delete(todo)
    db.session.commit()

    return redirect("/")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True, port=8080)
