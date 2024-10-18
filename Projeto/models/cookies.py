from flask import session

CAMPOS_LOGIN = ['nome']

def existe(campo):
    return campo in session

def get(campo):
    return session[campo]

def atualizar_login(nome):
    session['nome'] = nome

def limpar_login():
    for campo in CAMPOS_LOGIN:
        session.pop(campo, None)