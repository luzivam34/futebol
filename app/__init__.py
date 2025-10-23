from flask import Flask  # importação da Biblioteca Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


# função que cria o aplicativo
def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)

    # importação dos arquivos routes
    from .routes.main_route import mainBluePrint

    # registros das rotas blueprints
    app.register_blueprint(mainBluePrint)

    with app.app_context():
        db.create_all()

    return app
