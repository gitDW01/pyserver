from os import environ
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return '<form action="/echo" method="GET"><input name="text"><input type="submit" value="Echo"></form>'
 
@app.route("/echo")
def echo(): 
    return "You said: " + request.args.get('text', '')
 
app.run(environ.get('PORT'))
