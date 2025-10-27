from flask import Flask  # importação da Biblioteca Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()


# função que cria o aplicativo
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # importação dos arquivos routes
    from .routes.main_route import mainBluePrint
    from .routes.clube_route import clubeBluePrint
    from .routes.partidas_route import partidaBluePrint

    # registros das rotas blueprints
    app.register_blueprint(mainBluePrint)
    app.register_blueprint(clubeBluePrint)
    app.register_blueprint(partidaBluePrint)

    with app.app_context():
        db.create_all()

    return app
