from flask import Blueprint, jsonify, request
from service.garantia_estendida_service import GarantiaEstendidaService
from entity.garantia_estendida import GarantiaEstendida
from exceptions.garantia_estendida_existente import GarantiaExistente
from exceptions.id_inexistente_exception import IdInexistenteException
from exceptions.converte_data_exception import ConverteDataException
from datetime import datetime
from utils.functions import login_required, role_required

garantia_estendida_bp = Blueprint('garantia_estendida', __name__)

@garantia_estendida_bp.route('', methods=['GET'])
def get_all():
    garantia_estendida = GarantiaEstendidaService.get_all()
    return jsonify([g.to_dict() for g in garantia_estendida])

@garantia_estendida_bp.route('', methods=['POST'])
def add_garantia_estendida():
    data = request.get_json()
    try:
        garantia_estendida = GarantiaEstendida(id_garantia=data['id_garantia'], data_inicio=data['data_inicio'], data_fim=data['data_fim'], ativo=True)
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    try:
        garantia_estendida_salva = GarantiaEstendidaService.create(garantia_estendida)
        return jsonify(garantia_estendida_salva.to_dict()), 201
    except IdInexistenteException as iie:
        return jsonify({"Error": str(iie)}), 400
    except GarantiaExistente as ge:
        return jsonify({"Error": str(ge)}), 403
    except ValueError as ve:
        return jsonify({"Error": str(ve)}), 409
    except Exception as e:
        return jsonify({"Error": "Erro Inesperado, tente novamente mais tarde"}), 500

@garantia_estendida_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        garantia_estendida = GarantiaEstendidaService.delete(id)
        return jsonify({"Delete":garantia_estendida}), 200
    except IdInexistenteException as iie:
        return jsonify({"Error": str(iie)}), 404
    except Exception as e:
        return jsonify({"Error": "Erro Inesperado, tente novamente mais tarde"}), 500

@garantia_estendida_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    try:
        garantia_estendida = GarantiaEstendidaService.get_by_id(id)
        if garantia_estendida:
            return jsonify(garantia_estendida.to_dict()), 200
        else:
            return jsonify({"Error": "Garantia Estendida não encontrada"}), 404
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    
@garantia_estendida_bp.route('/<int:id_garantia>', methods=['PUT'])
def update(id_garantia):
    data = request.get_json()
    try:
        garantiaE = GarantiaEstendida(data_inicio=data['data_inicio'], data_fim=data['data_fim'], ativo=data['ativo'])
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
    try:
        garantiaE_atualizada = GarantiaEstendidaService.update(id_garantia, garantiaE)
        return jsonify(garantiaE_atualizada.to_dict()), 200
    except ConverteDataException as cde:
        return jsonify({'Error':str(cde)}), 400
    except ValueError as ve:
        return jsonify({'Error':str(ve)}), 400
    except IdInexistenteException as iie:
        return jsonify({'Error':str(iie)}), 400
    except Exception as e:
        return jsonify({'Error':str(e)}), 404
