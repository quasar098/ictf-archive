from flask import Flask, render_template, url_for, request, redirect, make_response
import sqlite3

app = Flask(__name__)

def checkCreds(username, password):
  con = sqlite3.connect('database.db')
  cur = con.cursor()
  try:
    content = cur.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'").fetchall()
  except:
    content = []
  cur.close()
  con.close()
  if content == []:
    return False
  else:
  	return True

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/user", methods=['POST'])
def user():
	username = request.form['username']
	password = request.form['password']
	if checkCreds(username, password) == True:
		return render_template("user.html")
	else:
		return render_template("nub.html")

if __name__ == "__main__":
  app.run(host = "0.0.0.0")
