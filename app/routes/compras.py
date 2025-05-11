from flask import Blueprint, request, jsonify
from app.db import inserir_compra, consultar_compra, consultar_compra_id, alterar_compra, apagar_compra

compras_bp = Blueprint('compras', __name__)

@compras_bp.route('/', methods=['GET'])
def api_consultar_compra():
    return consultar_compra()

@compras_bp.route('/<int:id>', methods=['GET'])
def api_consultar_compra_id(id):
    return consultar_compra_id(id=id)

@compras_bp.route('/alterar/<int:id>', methods=['PUT'])
def api_alterar_compra_id(id):
    return alterar_compra(id=id)

@compras_bp.route('/cadastro', methods=['POST'])
def api_criar_compra():
    data = request.get_json()
    inserir_compra(data['produto'], data['preco'], data['quantidade'])
    return jsonify({"mensagem": "Compra inserida com sucesso!"}), 201

@compras_bp.route('/apagar/<int:id>', methods=['DELETE'])
def api_apagar_compra(id):
    return apagar_compra(id=id)



