from flask import Blueprint, request, render_template, redirect, url_for, session
from controllers.cadastro import Usuarios

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        for usuario in Usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                session['usuario'] = nome  # Armazena o nome do usuário na sessão
                return redirect(url_for('principal.dashboard'))
    return render_template('login.html')
        
    flash('Nome ou senha incorretos!')  # Mensagem de erro se as credenciais estiverem erradas