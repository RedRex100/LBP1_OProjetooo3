from flask import session, flash, request, redirect, url_for, render_template, Blueprint
from models.model import Usuario, Usuarios

def adicionar(nome, senha):
    novo_usaurio = Usuario(nome, senha)
    Usuarios.append(novo_usaurio)

cadastro = Blueprint("cadastro", __name__)

@cadastro.route('/')
def inicio():
    return render_template('inicio.html')

@cadastro.route('/cadastro', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        adicionar(nome, senha)
        return redirect(url_for('login.logar'))
    return render_template('cadastro.html')


@cadastro.route('/logout')
def logout():
    session.pop('usuario', None)  # Remove o usuário da sessão
    return redirect(url_for('login.logar'))
