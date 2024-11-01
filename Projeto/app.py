from flask import Flask, request, redirect, url_for
from controllers.cadastro import cadastro
from controllers.login import login, session
from controllers.principal import principal
from controllers.loja import loja

app = Flask(__name__)
app.secret_key = 'senha ultra secreta'

app.register_blueprint(cadastro)
app.register_blueprint(login)
app.register_blueprint(principal)
app.register_blueprint(loja)

@app.before_request
def b4_request():
    if 'usuario' in session:
        if request.endpoint == 'login.logar':
            return  redirect(url_for('principal.dashboard'))

@app.after_request
def a_request(response):
    print("Depois da requisição")
    return response


if __name__ == '__main__':
     app.run(debug = True)