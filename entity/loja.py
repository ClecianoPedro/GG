from app import db

class Loja(db.Model):
    __tablename__ = 'loja'
    #ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #Nome
    nome = db.Column(db.String(128), nullable=False)
    #CNPJ
    cnpj = db.Column(db.String(17), unique=True, nullable=False)
    #Telefone
    telefone = db.Column(db.String(11))
    #Endereço
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))
    #RELACAO_GARANTIA
    garantias = db.relationship('Garantia', backref='loja', lazy=True)
    #URL
    url = db.Column(db.String(200))

    def to_dict(self):
        return {
            'id':self.id,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'telefone': self.telefone,
            'endereco': self.endereco.to_dict(),
            'url': self.url
        }
    
    def __str__(self):
        return self.nome + ' ' + self.cnpj + ' ' + self.telefone