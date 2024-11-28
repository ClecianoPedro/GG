from app import db
import datetime, pytz

class CodigoRecuperacao(db.Model):
    __tablename__ = 'codigo_recuperacao'

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    email_usuario = db.Column(db.String(200), primary_key=True, nullable=False)
    codigo = db.Column(db.String(6), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.datetime.now(pytz.timezone("America/Sao_Paulo")))
    expira_em = db.Column(db.DateTime, nullable=False)