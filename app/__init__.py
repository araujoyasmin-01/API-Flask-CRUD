from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    from .routes.compras import compras_bp
    app.register_blueprint(compras_bp, url_prefix='/api/compras')

    return app
