from entity.loja import Loja
from db import db

class LojaRepository:

    #Função buscar_todas
    @staticmethod
    def get_all():
        return Loja.query.all()
    
    #Buscar por ID
    @staticmethod
    def get_by_id(id):
        return Loja.query.get(id)
    
    #Buscar por CNPJ
    @staticmethod
    def get_by_cnpj(cnpj):
        return Loja.query.filter_by(cnpj=cnpj).first()
    
    #Criar Loja
    @staticmethod
    def create(loja):
        db.session.add(loja)
        db.session.commit()
        return loja
    
    #Atualizar Loja
    @staticmethod
    def update(id, loja):
        loja_antiga = LojaRepository.get_by_id(id)
        if loja_antiga:
            loja_antiga.nome = loja.nome
            loja_antiga.cnpj = loja.cnpj
            loja_antiga.telefone = loja.telefone
            db.session.add(loja_antiga)
            db.session.commit()
        return loja_antiga
    
    #Deletar Loja
    @staticmethod
    def delete(id):
        loja = LojaRepository.get_by_id(id)
        if loja:
            db.session.delete(loja)
            db.session.commit()
        return loja