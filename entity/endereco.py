from app import db

class Endereco(db.Model):
    __tablename__ = 'endereco'
    #ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #Rua
    logradouro = db.Column(db.String(100), nullable=False)
    #bairro
    bairro = db.Column(db.String(50), nullable=False)
    #numero
    numero = db.Column(db.String(24), nullable=False)
    #cep
    cep = db.Column(db.String(10), nullable=False)
    #cidade
    cidade = db.Column(db.String(100), nullable=False)
    #estado
    estado = db.Column(db.String(2), nullable=False)
    #Relacionamento com loja
    loja = db.relationship('Loja', backref='endereco', lazy=True)

    def to_dict(self):
        return{
            'id': self.id,
            'logradouro': self.logradouro,
            'bairro': self.bairro,
            'numero': self.numero,
            'cep': self.cep,
            'cidade': self.cidade,
            'estado': self.estado
        }
    
    def __str__(self):
        return self.logradouro + '\n' + self.bairro + '\n' + self.numero + '\n' + self.cep + '\n' + self.cidade + '\n' + self.estado