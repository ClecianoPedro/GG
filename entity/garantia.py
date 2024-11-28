from app import db
from datetime import datetime

class Garantia(db.Model):
    __tablename__ = 'garantia'

    #ID_GARANTIA
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #ID_USUARIO
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    #ID_PRODUTO
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id'))
    #ID_LOJA
    id_loja = db.Column(db.Integer, db.ForeignKey('loja.id'))
    #ID_DOCUMENTO
    id_documento = db.Column(db.Integer, db.ForeignKey('documento.id'))
    #APELIDO_GARANTIA
    apelido = db.Column(db.String(40))
    #DATA-INICIO
    data_inicio = db.Column(db.Date, nullable=False)
    #DATA-FIM
    data_fim = db.Column(db.Date, nullable=False)
    #ATIVO
    ativo = db.Column(db.Boolean, nullable=False)
    #RELACIONAMENTO_GARANTIA_ESTENDIDA
    garantia_estendida = db.relationship('GarantiaEstendida', backref='garantia', lazy=True)

    def to_dict(self):
        try:
            return {
            'id_garantia': self.id,
            'usuario': self.usuario.to_dict_resumida(), #Loop infinito
            'produto': self.produto.to_dict(),
            'loja': self.loja.to_dict(),
            'documento': self.documento.to_dict(),
            'apelido': self.apelido,
            'data_inicio': self.data_inicio.strftime('%d/%m/%Y'),
            'data_fim': self.data_fim.strftime('%d/%m/%Y'),
            'ativo': self.ativo
            }
        except Exception as e:
            raise e('Erro na conversão to_dict()')