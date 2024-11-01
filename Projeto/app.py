from flask import Flask, render_template, request, redirect, url_for, session, flash
from controllers.cadastro import adicionar, Usuarios

app = Flask(__name__)
app.secret_key = 'senha ultra secreta'

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        adicionar(nome, senha)
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        for usuario in Usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                session['usuario'] = nome  # Armazena o nome do usuário na sessão
                return redirect(url_for('dashboard'))
    return render_template('login.html')
        
    flash('Nome ou senha incorretos!')  # Mensagem de erro se as credenciais estiverem erradas

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return f'Bem-vindo, {session["usuario"]}! <a href="/logout">Sair</a>'

@app.route('/logout')
def logout():
    session.pop('usuario', None)  # Remove o usuário da sessão
    return redirect(url_for('login'))

if __name__ == '__main__':
     app.run(debug = True)