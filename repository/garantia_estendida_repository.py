from entity.garantia_estendida import GarantiaEstendida
from exceptions.id_inexistente_exception import IdInexistenteException
from db import db

class GarantiaEstendidaRepository:

    @staticmethod
    def get_all():
        '''Função para buscar tudo'''
        return GarantiaEstendida.query.all()
    
    @staticmethod
    def get_by_id(id):
        '''Função para buscar por id'''
        id_garantia_estendida = GarantiaEstendida.query.get(id)
        if id_garantia_estendida:
            return id_garantia_estendida
        else:
            raise IdInexistenteException('ID não encontrado')
    
    @staticmethod
    def create(garantia_estendida:object):
        '''Função para adicionar uma Garantia estentida'''
        try:
            db.session.add(garantia_estendida)
            db.session.commit()
            return garantia_estendida
        except Exception as e:
            db.session.rollback()
            raise e ('Erro inesperado ao adicionar uma garantia estendida')

    @staticmethod
    def delete(id):
        '''Função para deletar Garantia estentida'''
        db.session.delete(GarantiaEstendidaRepository.get_by_id(id))
        db.session.commit()
        return True

    @staticmethod
    def update(id:int, garantiaE_novo:object):
        try:
            garantiaE_novo.id = id
            db.session.add(garantiaE_novo)
            db.session.commit()
            return garantiaE_novo
        except Exception as e:
            db.session.rollback()