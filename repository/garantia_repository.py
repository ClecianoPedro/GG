from entity.garantia import Garantia
from db import db
from exceptions.id_inexistente_exception import IdInexistenteException

class GarantiaRepository:

    @staticmethod
    def get_all_warrantys():
        return Garantia.query.all()

    @staticmethod
    def get_warranty_by_id(id:int)-> object:
        return Garantia.query.get(id)
        
    @staticmethod
    def create_warranty(garantia:object):
        try:
            db.session.add(garantia)
            db.session.commit()
            return garantia
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_warranty(id:int, garantia_atualizada:object)-> object:
        try:
            garantia_atualizada.id = id
            db.session.add(garantia_atualizada)
            db.session.commit()
            return garantia_atualizada
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def delete_warranty(id:int):
        garantia = GarantiaRepository.get_warranty_by_id(id)
        if garantia:
            try:
                db.session.delete(garantia)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
        raise IdInexistenteException('ID não encontrado')