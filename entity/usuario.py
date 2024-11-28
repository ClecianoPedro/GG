from app import db
import enum

class Sexo(enum.Enum):
    masculino = 'masculino'
    feminino = 'feminino'

class Usuario(db.Model):
    __tablename__ = 'usuario'

    #ID_USUARIO
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #NOME
    nome = db.Column(db.String(43), nullable=False)
    #EMAIL
    email = db.Column(db.String(400), nullable=False, unique=True)
    #SENHA
    senha = db.Column(db.String(510), nullable=False)
    #SEXO
    sexo = db.Column(db.Enum(Sexo), nullable=False)
    #TELEFONE
    telefone = db.Column(db.String(11), unique=True)
    #PERMISSÕES
    role = db.Column(db.String(32), nullable=False) #User ou Admin
    #RELACIONAMENTO_GARANTIA
    garantias = db.relationship('Garantia', backref='usuario', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'sexo': self.sexo.value,
            'telefone': self.telefone,
            'garantias': [garantia.to_dict() for garantia in self.garantias]
        }

    def to_dict_resumida(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'sexo': self.sexo.value,
            'telefone': self.telefone
        }
