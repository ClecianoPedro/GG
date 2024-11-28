from entity.usuario import Usuario
from entity.codigo_recuperacao import CodigoRecuperacao
from db import db
from exceptions.id_inexistente_exception import IdInexistenteException
import random, pytz, datetime
from datetime import timedelta

class UsuarioRepository:
    
    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def get_user_by_id(id:int):
        return Usuario.query.get(id)
    
    @staticmethod
    def get_user_by_email(email:str)-> object:
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_phone(telefone:str)-> object:
        return Usuario.query.filter_by(telefone=telefone).first()

    @staticmethod
    def register(usuario:object) -> object:
        try:
            db.session.add(usuario)
            db.session.commit()
            return usuario
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update_user(id:int, usuario_atualizado:object):
        usuario = UsuarioRepository.get_user_by_id(id)
        try:
            usuario.nome = usuario_atualizado.nome
            usuario.email = usuario_atualizado.email
            usuario.sexo = usuario_atualizado.sexo
            usuario.telefone = usuario_atualizado.telefone
            db.session.add(usuario)
            db.session.commit()
            return usuario
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def delete_user(id:int):
        usuario = UsuarioRepository.get_user_by_id(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return True
        raise IdInexistenteException('ID não encontrado')
    
    @staticmethod
    def change_password(id:int, senha_nova:str):
        usuario = UsuarioRepository.get_user_by_id(id)
        usuario.senha = senha_nova
        db.session.commit()
        return True

    @staticmethod
    def recovery_code_generator(email:str):
        usuario = UsuarioRepository.get_user_by_email(email)
        codigo_gerado = str(random.randint(100000, 999999))
        expiracao = datetime.datetime.now(pytz.timezone('America/Sao_Paulo')) + timedelta(minutes=5)
        codigo_recuperacao = CodigoRecuperacao(id_usuario=usuario.id, email_usuario=email, codigo=codigo_gerado, expira_em=expiracao)
        db.session.add(codigo_recuperacao)
        db.session.commit()
        return True

    @staticmethod  
    def search_valid_code(email:str, codigo:str):
        return CodigoRecuperacao.query.filter_by(email_usuario=email, codigo=codigo).first()
    
    @staticmethod
    def delete_old_recovery_code(codigo_recuperacao:str):
        db.session.delete(codigo_recuperacao)
        db.session.commit()

    @staticmethod
    def delete_recovery_codes(email:str):
        db.session.query(CodigoRecuperacao).filter(CodigoRecuperacao.email_usuario==email).delete(synchronize_session=False)
