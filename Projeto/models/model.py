class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
Usuarios = []

def adicionar_usuario(login, senha):
    novo_usuario = Usuario(login, senha)
    Usuarios.append(novo_usuario)