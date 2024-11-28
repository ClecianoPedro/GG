from flask import Blueprint, request, jsonify
from entity.garantia import Garantia
from service.garantia_service import GarantiaService
from exceptions.id_inexistente_exception import IdInexistenteException
from exceptions.converte_data_exception import ConverteDataException
from utils.functions import login_required, role_required

garantia_bp = Blueprint('garantia', __name__)

@garantia_bp.route('', methods=['GET'])
@role_required(['Admin'])
def get_all_warrantys():
    try:
        garantias = GarantiaService.get_all_warrantys()
        return jsonify(garantias), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 404

@garantia_bp.route('/<int:id_garantia>', methods=['GET'])
@role_required(['Admin'])
def get_warranty_by_id(id_garantia): #Revisado
    try:
        garantia = GarantiaService.get_warranty_by_id(id_garantia)
        return jsonify(garantia.to_dict()), 200
    except IdInexistenteException as iie:
        return jsonify({'Eror':str(iie)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404

@garantia_bp.route('', methods=['POST'])
@login_required
def create_warranty(): #Revisado
    data = request.get_json()
    if not data['apelido']:
        apelido = None
    else:
        apelido = data['apelido']
    try:
        garantia = Garantia(id_usuario=data['id_usuario'], id_produto=data['id_produto'], id_loja=data['id_loja'], id_documento=data['id_documento'], apelido=apelido, data_inicio=data['data_inicio'], data_fim=data['data_fim'], ativo=True)
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    try:
        garantia_salva = GarantiaService.create_warranty(garantia)
        return jsonify(garantia_salva.to_dict()), 201
    except IdInexistenteException as iie:
        return jsonify({'Error':str(iie)}), 400
    except ConverteDataException as cde:
        return jsonify({'Error':str(cde)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404

@garantia_bp.route('/<int:id_garantia>', methods=['PUT'])
@login_required
def update_warranty(id_garantia):
    data = request.get_json()
    if not data['apelido']:
        apelido = None
    else:
        apelido = data['apelido']

    try:
        garantia = Garantia(apelido=apelido, data_inicio=data['data_inicio'], data_fim=data['data_fim'], ativo=data['ativo'])
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    try:
        garantia_atualizada = GarantiaService.update_warranty(id_garantia, garantia)
        return jsonify(garantia_atualizada.to_dict()), 200
    except ConverteDataException as cde:
        return jsonify({'Error':str(cde)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except IdInexistenteException as iie:
        return jsonify({'Error':str(iie)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404

@garantia_bp.route('/<id_garantia>', methods=['DELETE'])
@login_required
def delete_warranty(id_garantia):
    try:
        deleted_warranty = GarantiaService.delete_warranty(id_garantia)
        return jsonify({'Delete': deleted_warranty}), 200
    except IdInexistenteException as iie:
        return jsonify({'Error':str(iie)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
