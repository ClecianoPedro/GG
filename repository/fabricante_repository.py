from entity.fabricante import Fabricante
from exceptions.id_inexistente_exception import IdInexistenteException
from db import db

class FabricanteRepository:

    @staticmethod
    def get_all():
        '''Função para buscar todos os fabricantes'''
        return Fabricante.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Fabricante.query.get(id)
    
    @staticmethod
    def get_by_nome(nome):
        '''Função para buscar um fabricante pelo nome'''
        return Fabricante.query.filter_by(nome=nome).first()
    
    @staticmethod
    def create(fabricante):
        '''Função para adicionar um fabricante com tratamento de exceção'''
        try:
            db.session.add(fabricante)
            db.session.commit()
            return fabricante
        except Exception as e:
            db.session.rollback()
            raise e

    
    @staticmethod
    def delete(fabricante):
        '''Função para deletar um fabricante'''
        try:
            db.session.delete(fabricante)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e 
        

    @staticmethod
    def update(id:int, fabricante_novo:object):
        try:
            fabricante_novo.id = id
            db.session.add(fabricante_novo)
            db.session.commit()
            return fabricante_novo
        except Exception as e:
            db.session.rollback()
        
