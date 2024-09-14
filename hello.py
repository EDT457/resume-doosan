from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
    'test.html',name=name)

# Route for the basic hello
@app.route("/hello")
def hello_world():
    return "Hello World!"

# Route for members
@app.route("/members")
def members():
    return "Members"

# Route for member with a name parameter
@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
