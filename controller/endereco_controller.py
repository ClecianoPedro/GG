from flask import Blueprint, request, jsonify
from service.endereco_service import EnderecoService
from entity.endereco import Endereco
from exceptions.endereco_existente_exception import EnderecoExistenteException
from utils.functions import login_required, role_required

endereco_bp = Blueprint('endereco', __name__)

@endereco_bp.route('/<int:id>', methods=['GET'])
def get_endereco(id):
    try:
        endereco = EnderecoService.buscar_por_id(id)
        return jsonify(endereco.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error":str(e)}), 400
    
@endereco_bp.route('', methods=['GET'])
def get_enderecos():
    enderecos = EnderecoService.buscar_todos()
    return jsonify(enderecos)

@endereco_bp.route('/<int:id>', methods=['DELETE'])
def deletar_endereco(id):
    try:
        EnderecoService.deletar_por_id(id)
        return {"message": "Endereço deletado com sucesso!"}, 200
    except ValueError as e:
        return {"error": str(e)}, 404

@endereco_bp.route('', methods=['POST'])
def cadastrar_endereco():
    data = request.get_json()
    endereco = Endereco(logradouro=data['logradouro'],
                bairro=data['bairro'],
                numero=data['numero'],
                cep=data['cep'],
                cidade=data['cidade'],
                estado=data['estado']
    )
    try:
        endereco_salvo = EnderecoService.cadastrar_endereco(endereco)
        return jsonify(endereco_salvo.to_dict()), 201
    except EnderecoExistenteException as uee:
        return jsonify({"Error":str(uee)}), 403
    except ValueError as e:
        return jsonify({"Error":str(e)}), 409
    except Exception as ex:
        return jsonify({"Error":"Error Inesperado, tente novamente mais tarde"}), 500

    return 
