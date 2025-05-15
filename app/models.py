from app import db
from sqlalchemy import Column, Numeric

class ListaCompras(db.Model):
    __tablename__ = 'ListaCompras'
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String)
    preco = db.Column(db.Numeric(10,2))
    quantidade = db.Column(db.Integer)

class Usuarios(db.Model):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    senha_hash = db.Column(db.String)