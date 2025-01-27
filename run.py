#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def random_question():
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    return choice(questions)

def check_answer(q_id, a_id):
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    q = list(filter(lambda x: x["id"] == q_id, questions))[0]
    return q["correct"] == a_id



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question")
def question():
    return render_template("question.html", question=random_question())


@app.route("/answer/<int:question_id>/<int:answer_id>")
def answer(question_id, answer_id):
    correct = check_answer(question_id, answer_id)
    return render_template("answer.html", correct=correct)


@app.route("/Valentina")
def Valentina():
    return render_template("Valentina.html")


@app.route("/Fiona")
def Fiona():
    return render_template("Fiona.html", question=random_question())


@app.route("/Tim")
def Tim():
    return render_template("Tim.html", question=random_question())


@app.route("/Elion")
def Elion():
    return render_template("Elion.html", question=random_question())



if __name__ == "__main__":
    app.run()
