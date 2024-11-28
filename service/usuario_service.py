from repository.usuario_repository import UsuarioRepository
from exceptions.usuario_existente_exception import UsuarioExistenteException
from exceptions.id_inexistente_exception import IdInexistenteException
from exceptions.usuario_inexistente_exception import UsuarioInexistenteException
from exceptions.codigo_invalido_exception import CodigoInvalidoException
from utils.functions import send_recovery_code_to_mail
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt, pytz


class UsuarioService:

    @staticmethod
    def get_all():
        usuarios = UsuarioRepository.get_all()
        return [usuario.to_dict() for usuario in usuarios]

    @staticmethod
    def get_user_by_id(id:int, email:str):
        usuario = UsuarioRepository.get_user_by_email(email)
        if usuario:
            if usuario.id == id:
                return UsuarioRepository.get_user_by_id(id)
            raise ValueError('ID não corresponde ao usuário')
        raise IdInexistenteException('ID não encontrado')

    @staticmethod
    def get_user_by_email(email:str):
        email = UsuarioRepository.get_user_by_email(email)
        if email:
            return email
        raise IdInexistenteException('Email não encontrado')

    @staticmethod
    def register(usuario:object):
        if UsuarioRepository.get_user_by_email(usuario.email):
            raise UsuarioExistenteException('Email já cadastrado')
        elif usuario.telefone is not None:
            if UsuarioRepository.get_user_by_phone(usuario.telefone):
                raise UsuarioExistenteException('Telefone já cadastrado')
            
        elif len(usuario.nome) < 2 or len(usuario.nome) > 43:
            raise ValueError('Nome não pode ser menor que 2 caracteres ou maior que 43 caracteres')
        elif len(usuario.email) > 400:
            raise ValueError('Email maior que 400 caracteres')
        elif len(usuario.senha) < 8 or len(usuario.senha) > 20:
            raise ValueError('Senha deve conter entre 8 e 20 caracteres')

        #Transforma senha em Hash
        senha_hash = generate_password_hash(usuario.senha)
        usuario.senha = senha_hash
        return UsuarioRepository.register(usuario)
        
    @staticmethod
    def authentication(email:str, senha:str):
        usuario = UsuarioRepository.get_user_by_email(email)
        if usuario == None:
            raise UsuarioInexistenteException('Usuário inexistente')
        
        if check_password_hash(usuario.senha ,senha):
            payload = {
                'subject': usuario.email,
                'role' : usuario.role,
                'exp': datetime.now(pytz.timezone('America/Sao_Paulo')) + timedelta(minutes=30)
            }

            token = jwt.encode(payload, 'GGFAP', algorithm='HS256')
            return token
        return False

    @staticmethod
    def update_user(id:int, usuario:object):
        return UsuarioRepository.update_user(id, usuario)
        
    @staticmethod
    def change_password(id:int, senha_antiga:str, senha_nova:str):
        usuario = UsuarioRepository.get_user_by_id(id)
        if usuario == None:
            raise IdInexistenteException('ID inexistente')
        if len(senha_nova) < 8 or len(senha_nova) > 20:
            raise ValueError('Senha deve conter entre 8 e 20 caracteres')
        if check_password_hash(usuario.senha, senha_antiga):
            try:
                senha_nova = generate_password_hash(senha_nova)
            except Exception as e:
                raise e
            return UsuarioRepository.change_password(id, senha_nova)
        raise ValueError('Senha antiga errada')

    @staticmethod
    def delete_user(id:int, email:str):
        usuario = UsuarioRepository.get_user_by_email(email)
        if usuario:
            if usuario.id == id:
                return UsuarioRepository.delete_user(id)
            raise ValueError('ID não corresponde ao usuário')
        raise IdInexistenteException('Usuario inexistente')
        
    @staticmethod
    def password_recovery(email:str):
        mail = UsuarioRepository.get_user_by_email(email)
        if not mail:
            raise IdInexistenteException('Email não cadastrado no sistema') 
        UsuarioRepository.delete_recovery_codes(email)
        codigo_gerado = UsuarioRepository.recovery_code_generator(email)
        if codigo_gerado:
            send_recovery_code_to_mail(codigo_gerado, email)
            return True
        raise ValueError('Erro ao gerar código de recuperação')

    @staticmethod
    def reset_password(email:str, codigo:str, nova_senha:str):
        usuario = UsuarioRepository.get_user_by_email(email)
        if not usuario:
            raise IdInexistenteException('Email não encontrado')
        codigo_recuperacao = UsuarioRepository.search_valid_code(usuario.email, codigo)
        if not codigo_recuperacao:
            raise CodigoInvalidoException('Código inválido ou expirado')
        if len(nova_senha) < 8 or len(nova_senha) > 20:
            raise ValueError('Senha deve conter entre 8 e 20 caracteres')
        try:
            senha_hash = generate_password_hash(nova_senha)
        except Exception as e:
            raise e
        usuario_atualizado = UsuarioRepository.change_password(usuario.id, senha_hash)
        if usuario_atualizado:
            UsuarioRepository.delete_old_recovery_code(codigo_recuperacao)
            return True
