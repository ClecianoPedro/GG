from app import db
from  entity.categoria  import CategoriaEnum

class Produto(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(255))
    marca = db.Column(db.String(255))
    n_serie = db.Column(db.String(255), unique=True)

    categoria = db.relationship('Categoria', backref='produtos', lazy=True)
    garantias = db.relationship('Garantia', backref='produto', lazy=True)

    def to_dict(self):
        return {
            'id_produto':self.id,
            'categoria':self.categoria.nome.value,
            'nome':self.nome,
            'modelo':self.modelo,
            'marca':self.marca,
            'n_serie':self.n_serie
        }