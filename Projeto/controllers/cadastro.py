from flask import session, flash, request, redirect, url_for, render_template
from models.model import Usuario, Usuarios

def adicionar(nome, senha):
    novo_usaurio = Usuario(nome, senha)
    Usuarios.append(novo_usaurio)

def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        for usuario in Usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                session['usuario'] = nome  # Armazena o nome do usuário na sessão
                return redirect(url_for('dashboard'))
    return render_template('login.html')
        
    flash('Nome ou senha incorretos!')  
    # Mensagem de erro se as credenciais estiverem erradas