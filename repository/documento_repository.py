from entity.documento import Documento
from db import db

class DocumentoRepository:

    #função buscar_todos
    @staticmethod
    def get_all():
        return Documento.query.all()
    
    #buscar_por_ID
    @staticmethod
    def get_by_id(id):
        return Documento.query.get(id)
    
    #Criar Documento
    @staticmethod
    def create(documento):
        db.session.add(documento)
        db.session.commit()
        return documento
    
    #atualizar Documento
    @staticmethod
    def update(id, data):
        documento = DocumentoRepository.get_by_id(id)
        if documento:
            documento.descricao = data.get('descricao', documento.descricao)
            documento.url = data.get('url', documento.url)
            db.session.commit()
        return documento
    
    #Deletar Documento
    @staticmethod
    def delete(id):
        documento = DocumentoRepository.get_by_id(id)
        if documento:
            db.session.delete(documento)
            db.session.commit()
        return documento