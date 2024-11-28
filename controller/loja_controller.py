from flask import Blueprint, request, jsonify
from service.loja_service import LojaService
from entity.loja import Loja
from entity.endereco import Endereco
from exceptions.loja_existente_exception import LojaExistenteException
from exceptions.id_inexistente_exception import IdInexistenteException
from utils.functions import login_required, role_required

loja_bp = Blueprint('loja', __name__)

@loja_bp.route('/<int:id>', methods=['GET'])
def get_loja(id):
    try:
        loja = LojaService.buscar_por_id(id)
        return jsonify(loja.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error":str(e)}), 400

@loja_bp.route('', methods=['GET'])
def get_lojas():
    lojas = LojaService.buscar_todos()
    return jsonify(lojas)

@loja_bp.route('', methods=['POST'])
def cadastrar_loja():
    data = request.get_json()
    if not data['url']:
        url = None
    else:
        url = data['url']
    loja = Loja(nome=data['nome'],
                cnpj=data['cnpj'],
                telefone=data['telefone'],
                url=url
                )
    endereco = Endereco(logradouro=data['endereco']['logradouro'], bairro=data['endereco']['bairro'], numero=data['endereco']['numero'],
                        cep=data['endereco']['cep'], cidade=data['endereco']['cidade'], estado=data['endereco']['estado'])

    try:
        loja_salvo = LojaService.cadastrar_loja(loja, endereco)
        return jsonify(loja_salvo.to_dict()), 201
    except LojaExistenteException as uee:
        return jsonify({"Error":str(uee)}), 403
    except ValueError as e:
        return jsonify({"Error":str(e)}), 409
    except Exception as ex:
        return jsonify({"Error":"Error Inesperado, tente novamente mais tarde"}), 500

    return   

@loja_bp.route('/<int:id>', methods=['DELETE'])
def deletar_loja(id):
    try:
        LojaService.deletar_por_id(id)
        return {"message": "Loja deletado com sucesso"}, 200
    except ValueError as e:
        return {"error": str(e)}, 404

@loja_bp.route('/<int:id>', methods=['PUT'])
def update_loja(id):
    data = request.json  # Recebe os dados do corpo da requisição
    loja = Loja(nome=data['nome'],
                cnpj=data['cnpj'],
                telefone=data['telefone'])
    
    endereco = Endereco(logradouro=data['endereco']['logradouro'], bairro=data['endereco']['bairro'], numero=data['endereco']['numero'],
                        cep=data['endereco']['cep'], cidade=data['endereco']['cidade'], estado=data['endereco']['estado'])
    
    try:
        response = LojaService.update_loja(id, loja, endereco)
        return jsonify(response.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404