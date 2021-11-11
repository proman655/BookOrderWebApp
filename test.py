from flask import Flask

app = Flask(myproject)

@app.route("/")

def hello_world():
    return "<p>Hello, World!</p>"