from app import db

class Fabricante(db.Model):
    __tablename__ = "fabricante"

    id_fabricante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(11))

    def to_dict(self):
            return {
                'id_fabricante': self.id_fabricante,
                'nome': self.nome,
                'cnpj': self.cnpj,
                'telefone': self.telefone
            }
    
    def __repr__(self):
        return f"<Fabricante(id={self.id_fabricante}, nome={self.nome})>"
