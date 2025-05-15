from flask import Flask
import jwt
from flask_sqlalchemy import SQLAlchemy
from config import JWT_SECRET_KEY
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    
    db.init_app(app)

    from .routes.compras import compras_bp
    app.register_blueprint(compras_bp, url_prefix='/api/compras')

    return app
