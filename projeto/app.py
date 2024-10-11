from flask import Flask, render_template
from models import Usuarios

app = Flask(__name__)

@app.route("/")
def render1():
    return render_template("pm.html")

@app.route("/login")
def render2():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
