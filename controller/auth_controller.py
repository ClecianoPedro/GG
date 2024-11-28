from flask import request, jsonify, Blueprint
from entity.usuario import Usuario, Sexo
from service.usuario_service import UsuarioService
from exceptions.usuario_existente_exception import UsuarioExistenteException
from exceptions.id_inexistente_exception import IdInexistenteException
from exceptions.codigo_invalido_exception import CodigoInvalidoException
from exceptions.usuario_inexistente_exception import UsuarioInexistenteException
from email_validator import EmailNotValidError
from utils.functions import role_required, format_string, verify_phone_number, validate_email_with_domain

auth_bp = Blueprint('autenticacao', __name__)

@auth_bp.route('/register', methods=['POST']) #Revisado
def register():
    data = request.get_json()
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

    try:
        usuario = Usuario(nome=format_string(data['nome'], 'nome'), email=email, senha=data['senha'], sexo=Sexo(format_string(data['sexo'], 'Sexo')), telefone=telefone, role='User')
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except EmailNotValidError as enve:
        return jsonify({'Error':str(enve)}), 400
    except AttributeError as ae:
        return jsonify({'Error':str(ae)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    
    try:
        usuario_salvo = UsuarioService.register(usuario)
        return jsonify(usuario_salvo.to_dict()), 201
    except UsuarioExistenteException as uee:
        return jsonify({'Error':str(uee)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    
@auth_bp.route('/register/admin', methods=['POST'])
@role_required(['Admin'])
def register_admin():  #Revisado
    data = request.get_json()
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
        telefone = verify_phone_number(data['telefone'], 'Telefone')

    try:
        user_admin = Usuario(nome=format_string(data['nome'], 'nome'), email=email, senha=data['senha'], sexo=Sexo(format_string(data['sexo'], 'Sexo')), telefone=telefone, role='Admin')
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except EmailNotValidError as enve:
        return jsonify({'Error':str(enve)}), 400
    except AttributeError as ae:
        return jsonify({'Error':str(ae)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    
    try:
        user_admin_registered = UsuarioService.register(user_admin)
        return jsonify(user_admin_registered.to_dict()), 201
    except UsuarioExistenteException as uee:
        return jsonify({'Error':str(uee)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404

@auth_bp.route('/login', methods=['POST'])
def login(): #Revisado
    data = request.get_json()
    try:
        token = UsuarioService.authentication(data['email'], data['senha'])
        if token:
            return jsonify({'Token': str(token)}), 200
        else:
            return jsonify({'Token': str(token)}), 400
    except UsuarioInexistenteException as uie:
        return jsonify({'Error': str(uie) }), 400
    except Exception as e:
        return jsonify({'Error': str(e) }), 404

@auth_bp.route('/password_recovery', methods=['POST'])
def password_recovery(): #Revisado
    data = request.get_json()
    email = data['email']
    try:
        email_usuario = UsuarioService.password_recovery(email)
        return jsonify({'Send Email': email_usuario}), 200
    except ValueError as ve:
        return jsonify({'Error': str(ve)}), 400
    except IdInexistenteException as iie:
        return jsonify({'Error': str(iie)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

@auth_bp.route('/reset_password', methods=['POST'])
def reset_password(): #Revisado
    data = request.get_json()
    email = data['email']
    codigo = data['codigo']
    nova_senha = data['nova_senha']
    try:
        return jsonify({'Senha alterada': UsuarioService.reset_password(email, codigo, nova_senha)}), 308
    except ValueError as ve:
        return jsonify({'Error': str (ve)}), 400
    except IdInexistenteException as iie:
        return jsonify({'Error': str (iie)}), 400
    except CodigoInvalidoException as cie:
        return jsonify({'Error': str (cie)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 404