from app import db

class Documento(db.Model):
    __tablename__ = 'documento'
    #ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #DESCRIÇÃO
    descricao = db.Column(db.String(200), nullable=False)
    #IMAGEM
    url = db.Column(db.String(510), nullable=False)
    #RELACIONAMENTO_GARANTIA
    garantia = db.relationship('Garantia', backref='documento', lazy=True)
    

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'url': self.url
        }
    
    def __str__(self):
        return self.descricao + ' ' + self.url