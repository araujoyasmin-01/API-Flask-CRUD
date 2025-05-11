# API-Flask-CRUD
Criação e consulta de API com flaks, comunicando com banco de dados sql
# 🛒 API de Compras (Flask + SQL Server)

Este projeto é uma API REST desenvolvida com **Flask**, conectando-se ao **SQL Server** para realizar operações de **CRUD** usando **Stored Procedures**. A aplicação permite o gerenciamento de itens de compras com campos de produto, preço e quantidade.

---

## 🚀 Funcionalidades

- ✅ Criar compra (`POST /api/compras/cadastro`)
- 📄 Listar todas as compras (`GET /api/compras`)
- 🔍 Buscar compra por ID (`GET /api/compras/<id>`)
- ✏️ Atualizar compra (`PUT /api/compras/alterar/<id>`)
- ❌ Deletar compra (`DELETE /api/compras/apagar/<id>`)

---

---

## 🗂️ Banco de Dados

- Banco: `ComprasDB`
- Tabela: `ListaCompras`
- Conectividade: `PyODBC` + `SQLAlchemy`
- Todas as operações CRUD são feitas via Stored Procedures.

### 📜 Procedures criadas:

- `sp_INSERIR_COMPRA`
- `sp_ATUALIZAR_COMPRA` *(atualiza apenas os campos informados via `COALESCE`)*
- `sp_EXCLUIR_COMPRA`

---
## 🛠️ Tecnologias

- Python 3.x
- Flask
- SQLAlchemy
- PyODBC
- Microsoft SQL Server

---


