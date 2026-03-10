# app.py
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from models.user import db, User
from routes.routes_user import user_bp
from flask_sqlalchemy import SQLAlchemy
from controllers import db

def create_app():
    app = Flask(__name__)

    # Configuración básica
    app.config['SECRET_KEY'] = 'clave-secreta-super-segura'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/juegos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    CSRFProtect(app)
    db = SQLAlchemy(app)

    # Registrar Blueprints
    app.register_blueprint(user_bp)

    # Crear tablas si no existen
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
