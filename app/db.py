from . import db
from sqlalchemy import text
from app.models import ListaCompras, Usuarios
from flask import jsonify, request, make_response
from decimal import Decimal
import jwt
from datetime import datetime, timezone, timedelta
from config import JWT_SECRET_KEY

from functools import wraps

def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'mensagem': 'Token não foi incluido'}), 401
        
        try:
            resultado = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            usuario = Usuarios.query.filter_by(id=resultado['id']).first()           
        except:
            return jsonify({'mensagem':'Token invalido'}), 401
        return f(usuario, *args, **kwargs)
    return decorated
    
def validar_login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Login invalido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})
    usuario = Usuarios.query.filter_by(username=auth.username).first()
    if not usuario:
        return make_response('Login invalido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})
    if auth.password == usuario.senha_hash:
        token = jwt.encode({'id':usuario.id, 'exp': datetime.now(timezone.utc) + timedelta(minutes=30)}, JWT_SECRET_KEY)
        return jsonify({'token':token})
    return make_response('Login invalido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})

    

def consultar_compra():
    compras = ListaCompras.query.all()
    lista_compras = []
    try:
        for compra in compras:
            compra_atual = {}
            compra_atual['produto'] = compra.produto
            compra_atual['preco'] = compra.preco
            compra_atual['quantidade'] = compra.quantidade
            lista_compras.append(compra_atual)
        return jsonify({"compras":lista_compras})
    except Exception as e:
        return jsonify({"erro": str(e)})

def consultar_compra_id(id):
    compras = ListaCompras.query.filter_by(id=id).first()
    lista_compras = {}
    try:
        lista_compras['produto'] = compras.produto
    except:
        pass
    try:
        lista_compras['preco'] = compras.preco
    except:
        pass
    try:
        lista_compras['quantidade'] = compras.quantidade
    except:
        pass
    return jsonify({"item":lista_compras})

def inserir_compra(produto, preco, quantidade):
    with db.engine.connect() as conn:
        conn.execute(
            text("EXEC sp_INSERIR_COMPRA :Produto, :Preco, :Quantidade"),
            {"Produto": produto, "Preco": preco, "Quantidade": quantidade}
        )
        conn.commit()

def alterar_compra(id):
    compra_alterada = request.get_json()
    #compra = ListaCompras.query.filter_by(id=id).first()

    produto = compra_alterada.get('produto')
    preco = compra_alterada.get('preco')
    quantidade = compra_alterada.get('quantidade')

    try:
        with db.engine.connect() as conn:
            conn.execute(
                text("EXEC sp_ATUALIZAR_COMPRA :ID, :Produto, :Preco, :Quantidade"),
                {"ID":id, "Produto": produto, "Preco": preco, "Quantidade":quantidade}
            )
            conn.commit()
        return jsonify({"mensagem": "item atualizado com sucesso"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
def apagar_compra(id):
    try:
        with db.engine.connect() as conn:
            conn.execute(
                text("EXEC sp_EXCLUIR_COMPRA :ID"),
                {"ID":id}
            )
            conn.commit()
        return jsonify({"mensagem":"Item excluido da lista"})
    except Exception as e:
        return jsonify({"erro":str(e)})


