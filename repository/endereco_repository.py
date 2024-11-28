from entity.endereco import Endereco
from db import db

class EnderecoRepository:

    #Funcão buscar_todos:
    @staticmethod
    def get_all():
        return Endereco.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Endereco.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return Endereco.query.get(name)
    
    @staticmethod
    def create(endereco):
        db.session.add(endereco)
        db.session.commit()
        return endereco
    
    @staticmethod
    def delete(id):
        endereco = EnderecoRepository.get_by_id(id)
        if endereco:
            db.session.delete(endereco)
            db.session.commit()
        return endereco
    
    @staticmethod
    def update(id, endereco_atualizado):
        endereco = EnderecoRepository.get_by_id(id)
        if endereco:
            endereco.logradouro = endereco_atualizado.logradouro
            endereco.bairro = endereco_atualizado.bairro
            endereco.numero = endereco_atualizado.numero
            endereco.cep = endereco_atualizado.cep
            endereco.cidade = endereco_atualizado.cidade
            endereco.estado = endereco_atualizado.estado
        db.session.add(endereco)
        db.session.commit()
        return endereco