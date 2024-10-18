from flask import Flask, render_template, session, request, redirect, url_for
from models.model import adicionar_usuario
from models import cookies


app = Flask(__name__)
app.register_blueprint(login.c)
app.secret_key = '1234'

@app.before_request
def b4_request():
    if request.path == '/login':
        return 
    if not cookies.existe('nome'):
        return redirect(url_for('login.login'))

@app.after_request
def a_request(response):
    print("Depois da requisição")
    return response

@app.route('/')
def index():
    return render_template('index.html', nome=cookies.get('nome'))

if __name__ == '__main__':
    app.run(debug=True)