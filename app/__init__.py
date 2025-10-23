from flask import Flask # importação da Biblioteca Flask

# função que cria o aplicativo
def create_app():
    app = Flask(__name__)
    return app
