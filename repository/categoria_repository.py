from entity.categoria import Categoria
from db import db

class CategoriaRepository:

    @staticmethod
    def get_all():
        return Categoria.query.all()
    
    @staticmethod
    def get_by_name(nome):
        return Categoria.query.filter_by(nome=nome).first()
    
    @staticmethod
    def get_by_id(id):
        return Categoria.query.get(id)
    
    @staticmethod
    def create(categoria):
        try:
            db.session.add(categoria)
            db.session.commit()
            return categoria
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def delete(categoria):
        try:
            db.session.delete(categoria)
            db.session.commit()
            return True
        except Exception as e:
            raise e
        
    @staticmethod
    def update(id, data):
        categoria = CategoriaRepository.get_by_id(id)
        if categoria:
            categoria.nome = data['nome']
            db.session.commit()
            return categoria