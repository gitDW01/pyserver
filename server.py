from os import environ
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return '<form action="/echo" method="GET"><input name="text"><input type="submit" value="Echo"></form>'
 
@app.route("/echo")
def echo(): 
    return "You said: " + request.args.get('text', '')

if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)    
