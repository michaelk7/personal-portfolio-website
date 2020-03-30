from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

@app.route("/test")
def test():
	return "<h1 align='center'>Test</h1>"

@app.route("/home")
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/aboutme")
def aboutme():
	return render_template("aboutMe.html")

@app.route("/projects")
def projects():
	return render_template("projects.html")

@app.route("/contactme")
def contactme():
	return render_template("contactMe.html")

if __name__ == "__main__":
	app.run(debug=True)
