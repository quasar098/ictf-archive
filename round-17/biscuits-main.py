import os
from flask import Flask, render_template, url_for, request, redirect, make_response
import base64

app = Flask(__name__)

def auth(username):
	a = username.encode('ascii')
	b = base64.b64encode(a)
	c = b.decode('ascii')
	auth = ""
	for n in c:
		n = ord(n)
		n -= 4
		n += 1
		n = chr(n)
		auth += n
	auth = auth*2
	a = auth.encode('ascii')
	b = base64.b64encode(a)
	auth = b.decode('ascii')
	return auth

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/user", methods=['POST'])
def user():
	username = request.form['username']
	resp = make_response(render_template('user.html'))
	resp.set_cookie('TOKEN', auth(username))
	if request.cookies.get('TOKEN') == os.environ["token"]:
		return resp
	else:
		return render_template('fail.html')

if __name__ == "__main__":
  app.run(host = "0.0.0.0") 
