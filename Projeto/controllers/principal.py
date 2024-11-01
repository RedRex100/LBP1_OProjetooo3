from flask import Blueprint, render_template, redirect, url_for
from controllers.cadastro import session

principal = Blueprint('principal', __name__)

@principal.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login.logar'))
    return render_template("index.html", usuario = session['usuario'])