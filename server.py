from flask import Flask, request, render_template, redirect, session
import random

def randNum():
	rNum= random.randrange(0, 101)

	return rNum

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():

	# session["response"] = "e"

	answer = randNum()
	session["answer"] = answer

	result = request.form["guess"]
	session["result"] = result

	if str(session["result"]) < str(session["answer"]):
		session["response"] = "low"
	elif str(session["result"]) > str(session["answer"]):
		session["response"] = "high"
	elif str(session["result"]) == str(session["answer"]):
		session["response"] = "correct"

	return render_template("result.html")

app.run(debug = True)
