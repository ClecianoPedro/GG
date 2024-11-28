from flask import Blueprint, request, jsonify
from entity.usuario import Usuario, Sexo
from service.usuario_service import UsuarioService
from exceptions.id_inexistente_exception import IdInexistenteException
from email_validator import EmailNotValidError
from utils.functions import login_required, role_required, format_string, validate_email_with_domain, verify_phone_number

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('', methods=['GET'])
@role_required(['Admin'])
def get_all(): #Revisado
    try:
        usuarios = UsuarioService.get_all()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

@usuario_bp.route('/<int:id_usuario>', methods=['GET'])
@login_required
def get_user_by_id(id_usuario): #Verificar se o id do usuário bate com o id cadastrado para o mesmo usuário
    try:
        usuario = UsuarioService.get_user_by_id(id_usuario, request.user_email)
        return jsonify(usuario.to_dict()), 200
    except IdInexistenteException as iie:
        return jsonify({'Error': str(iie)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

@usuario_bp.route('/<int:id_usuario>/change_password', methods=['PUT'])
@login_required
def change_password(id_usuario): #Revisado
    data = request.get_json()
    try:
        senha = UsuarioService.change_password(id_usuario, senha_antiga=data['senha_antiga'], senha_nova=data['senha_nova'])
        return jsonify({'Senha alterada': senha})
    except IdInexistenteException as iie:
        return jsonify({'Error': str(iie)}), 400
    except ValueError as ve:
        return jsonify({'Error': str(ve)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

@usuario_bp.route('/<int:id_usuario>', methods=['PUT'])
@login_required
def update_user(id_usuario): #Revisado
    data = request.get_json()
    try:
        usuario = UsuarioService.get_user_by_email(request.user_email)
        if usuario.role == 'Admin':
            role = 'Admin'
        else:
            role = 'User'
    except IdInexistenteException as iie:
        return jsonify({'Error': str(iie)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

    try:
        validate_email_with_domain(data['email'])
        email = data['email']
    except EmailNotValidError as enve:
        return jsonify({'Error':str(enve)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404
    
    if not data['telefone']:
        telefone = None
    else:
        try:
            telefone = verify_phone_number(data['telefone'], 'Telefone')
        except ValueError as ve:
            return jsonify({'Error':str(ve)}), 400
        except AttributeError as ae:
            return jsonify({'Error':str(ae)}), 400
        except Exception as e:
            return jsonify({'Error':str(e)}), 404

    try:
        usuario = Usuario(nome=format_string(data['nome'], 'nome'), email=email, sexo=Sexo(format_string(data['sexo'], 'Sexo')), telefone=telefone, role=role)
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except EmailNotValidError as enve:
        return jsonify({'Error':str(enve)}), 400
    except AttributeError as ae:
        return jsonify({'Error':str(ae)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    
    try:
        usuario_atualizado = UsuarioService.update_user(id_usuario, usuario)
        return jsonify(usuario_atualizado.to_dict_resumida()), 200
    except ValueError as ve:
        return jsonify({'Error': str(ve)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404
    
@usuario_bp.route('/<int:id_usuario>', methods=['DELETE'])
@login_required
def delete_user(id_usuario): #Revisado
    try:
        deleted_user = UsuarioService.delete_user(id_usuario, request.user_email)
        return jsonify({'Delete': deleted_user}), 200
    except IdInexistenteException as iie:
        return jsonify({'Error': str(iie)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404
    