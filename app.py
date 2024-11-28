from flask import Flask
from config import Config
from db import db
import init_db

from controller.fabricante_controller import Fabricante_bp
from controller.categoria_controller import categoria_bp
from controller.endereco_controller import endereco_bp
from controller.documento_controller import documento_bp
from controller.garantia_controller import garantia_bp
from controller.loja_controller import loja_bp
from controller.produto_controller import produto_bp
from controller.usuario_controller import usuario_bp
from controller.garantia_estendida_controller import garantia_estendida_bp
from controller.auth_controller import auth_bp

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = "/static/upload"

db.init_app(app)

init_db.init_db(app)

app.register_blueprint(Fabricante_bp, url_prefix='/fabricante')
app.register_blueprint(categoria_bp, url_prefix='/categoria')
app.register_blueprint(endereco_bp, url_prefix='/endereco')
app.register_blueprint(documento_bp, url_prefix='/documento')
app.register_blueprint(garantia_bp, url_prefix='/garantia')
app.register_blueprint(loja_bp, url_prefix='/loja')
app.register_blueprint(produto_bp, url_prefix='/produto')
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(garantia_estendida_bp, url_prefix='/garantia_estendida')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)
