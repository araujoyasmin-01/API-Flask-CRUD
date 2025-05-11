from . import db
from sqlalchemy import text
from app.models import ListaCompras
from flask import jsonify, request
from decimal import Decimal


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


