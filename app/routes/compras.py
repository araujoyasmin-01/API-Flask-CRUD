from flask import Blueprint, request, jsonify
from app.db import inserir_compra, consultar_compra, consultar_compra_id, alterar_compra, apagar_compra, validar_login, token_obrigatorio

compras_bp = Blueprint('compras', __name__)

@compras_bp.route('/login')
def login():
    return validar_login()

@compras_bp.route('/', methods=['GET'])
@token_obrigatorio
def api_consultar_compra(usuario):
    return consultar_compra()

@compras_bp.route('/<int:id>', methods=['GET'])
@token_obrigatorio
def api_consultar_compra_id(usuario,id):
    return consultar_compra_id(id=id)

@compras_bp.route('/alterar/<int:id>', methods=['PUT'])
@token_obrigatorio
def api_alterar_compra_id(usuario,id):
    return alterar_compra(id=id)

@compras_bp.route('/cadastro', methods=['POST'])
@token_obrigatorio
def api_criar_compra(usuario):
    data = request.get_json()
    inserir_compra(data['produto'], data['preco'], data['quantidade'])
    return jsonify({"mensagem": "Compra inserida com sucesso!"}), 201

@compras_bp.route('/apagar/<int:id>', methods=['DELETE'])
@token_obrigatorio
def api_apagar_compra(usuario,id):
    return apagar_compra(id=id)
