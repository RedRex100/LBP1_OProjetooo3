from flask import Blueprint, request, json, render_template, make_response
from models.carrinho import materiais


loja = Blueprint('loja', __name__)

@loja.route('/loja')
def comprar():
    carrinho = request.cookies.get('carrinho')
    if carrinho:
        carrinho = json.loads(carrinho)
    else:
        carrinho = []
        
    total = sum(item['quantidade'] * next(m['preco'] for m in materiais if m['nome'] == item['material']) for item in carrinho)
    
    return render_template('loja.html', carrinho=carrinho, total = total)

@loja.route('/adicionar', methods=['POST'])
def adicionar():
    material = request.form['material']
    quantidade = int(request.form['quantity'])

    # Tenta obter o cookie do carrinho
    carrinho = request.cookies.get('carrinho')
    if carrinho:
        carrinho = json.loads(carrinho)
    else:
        carrinho = []

    # Adiciona o novo item ao carrinho
    carrinho.append({'material': material, 'quantidade': quantidade})

    # Armazena o carrinho no cookie
    resposta = make_response(render_template('loja.html', carrinho=carrinho, total=0))
    resposta.set_cookie('carrinho', json.dumps(carrinho), max_age=60*60*24) 

    return resposta