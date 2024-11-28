from app import db
from datetime import datetime

class GarantiaEstendida(db.Model):
    __tablename__ = "garantia_estendida"

    id_garantia_estendida = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_garantia = db.Column(db.Integer, db.ForeignKey('garantia.id'), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
            return {
                'id_garantia_estendida': self.id_garantia_estendida,
                'garantia': self.garantia.to_dict(),
                'data_inicio': self.data_inicio.strftime("%d/%m/%Y"),
                'data_fim': self.data_fim.strftime("%d/%m/%Y"),
                'ativo': self.ativo
            }
    
    def __repr__(self):
        return f"<GarantiaEstendida(id={self.id_garantia_estendida})>"