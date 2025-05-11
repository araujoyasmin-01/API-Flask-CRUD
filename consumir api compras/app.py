import requests
from pprint import pprint

# # GET ID
# lista_compras = requests.get('http://localhost:5000/api/compras/')
# pprint(lista_compras.json())
# item_lista = lista_compras.json()['item']

# preco = item_lista['preco']
# produto = item_lista['produto']
# quantidade = item_lista['quantidade']

# produto = "Arroz"
# preco = "13"
# quantidade = 1

# novo_item = {
#     'preco': preco,
#     'produto': produto,
#     'quantidade': quantidade
# }
# # POST
# incluir_item = requests.post('http://localhost:5000/api/compras/cadastro', json=novo_item)
# pprint(incluir_item.json())

# PUT
alteracao = {'preco':50}
alterar_item = requests.put('http://localhost:5000/api/compras/alterar/6', json=alteracao)
pprint(alterar_item.json())

# print(alterar_item.status_code)
# print(alterar_item.text)


# # DELETE
# apagar_item = requests.delete('http://localhost:5000/api/compras/apagar/4')
# pprint(apagar_item.json())