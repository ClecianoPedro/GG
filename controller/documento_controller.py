from flask import Blueprint, request, jsonify
from service.documento_service import DocumentoService
from entity.documento import Documento
from exceptions.documento_existente_exception import DocumentoExistenteException
from utils.functions import login_required, role_required

documento_bp = Blueprint('documento', __name__)

#buscar por ID
@documento_bp.route('/<int:id>', methods=['GET'])
def get_documento(id):
    try:
        documento = DocumentoService.buscar_por_id(id)
        return jsonify(documento.to_dict()), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400

#buscar Todos
@documento_bp.route('', methods=['GET'])
def get_documentos():
    documentos = DocumentoService.buscar_todos()
    return jsonify(documentos)

#upload arquivo
@documento_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']

        caminho = DocumentoService.upload_file(file)

        return jsonify({"Caminho": caminho}), 201
    return 'Arquivo não carregado!'

#cadastrar
@documento_bp.route('', methods=['POST'])
def cadastrar_documentos():
    data = request.get_json()
    documento = Documento(descricao = data['descricao'],
                          url = data['url']
                          )
    #dados de garantia caso seja edita aqui

    try:
        documento_salvo = DocumentoService.cadastrar_documento(documento)
        return jsonify(documento_salvo.to_dict()), 201
    except DocumentoExistenteException as dee:
        return jsonify({"error":str(dee)}), 403
    except ValueError as e:
        return jsonify({"Error":str(e)}), 409
    except Exception as ex:
        return jsonify({"Error":"Error Inesperado, tente novamente mais tarde"}), 500
    
    return

#deletar
@documento_bp.route('/<int:id>', methods=['DELETE'])
def deletar_documento(id):
    try:
        DocumentoService.deletar_por_id(id)
        return {"message": "Documento deletado com sucesso!"}, 200
    except ValueError as e:
        return {"error": str(e)}, 404
    
#Atualizar
@documento_bp.route('/<int:id>', methods=['PUT'])
def update_documento(id):
    data = request.json  # Recebe os dados do corpo da requisição
    try:
        response = DocumentoService.update_documento(id, data)
        return jsonify(response), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404