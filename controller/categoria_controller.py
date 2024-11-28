from flask import Blueprint, jsonify, request
from service.categoria_service import CategoriaService
from entity.categoria import Categoria, CategoriaEnum
from utils.functions import role_required, login_required, format_string, normalize_text
from exceptions.categoria_exception import CategoriaExistente, CategoriaNaoEncontrada, CategoriaSemNome
import unicodedata
categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/<nome>', methods=['GET'])
def get_categoria(nome):
    try:
        categoria = CategoriaService.buscar_por_nome(nome)
        return jsonify(categoria.to_dict()), 200
    except CategoriaNaoEncontrada as cne:
        return jsonify({"Error":str(cne)}), 404
    
@categoria_bp.route('/<int:id>', methods=['GET'])
def get_categoria_id(id):
    try:
        categoria = CategoriaService.buscar_por_id(id)
        return jsonify(categoria.to_dict()), 200
    except CategoriaNaoEncontrada as cne:
        return jsonify({'Error':str(cne)}), 404
    
@categoria_bp.route('', methods=['GET'])
def get_categorias():
    categorias = CategoriaService.buscar_todas()
    return jsonify(categorias)

def remover_acentos(nome):
    # Remove os acentos e caracteres especiais
    return ''.join(
        c for c in unicodedata.normalize('NFD', nome) if unicodedata.category(c) != 'Mn'
    )

@categoria_bp.route('', methods=['POST'])
# @role_required(['Admin'])
def cadastrar_categoria():
    data = request.get_json()

    nome = data['nome'].strip()
    if not nome:
        return jsonify({"Error": "O campo nome não pode ser vazio"}), 400
    if any(char.isdigit() for char in data['nome']):
        return jsonify({"Error": "O campo nome não pode conter números."}), 400

    # Normaliza o nome para remover acentos e converte para maiúsculas
    nome_normalizado = remover_acentos(nome).upper().replace(" ", "_")

    try:
        categoria = Categoria(nome=CategoriaEnum[nome_normalizado])  # Verifica se o nome é válido no Enum
    except KeyError:
        return jsonify({"Error": "Categoria inválida"}), 400

    try:
        categoria_salva = CategoriaService.cadastrar_categoria(categoria)
        return jsonify(categoria_salva.to_dict()), 201
    except CategoriaExistente as ce:
        return jsonify({"Error":str(ce)}), 400
    except ValueError as e:
        return jsonify({"Error":str(e)}), 400
    except CategoriaSemNome as csn:
        return jsonify({'Error':str(csn)}), 400
    except Exception as ex:
        return jsonify({"Error":str(ex)}), 500
    
@categoria_bp.route('/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    try:
        categoria_deletada = CategoriaService.delete(id)
        return jsonify({'Delete': categoria_deletada}), 200
    except CategoriaNaoEncontrada as cne:
        return jsonify({'Error':str(cne)}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
@categoria_bp.route('/<int:id>', methods=['PUT'])
def update_categoria(id):
    data = request.json  # Recebe os dados do corpo da requisição
    nome = data['nome'].strip()
    if not nome:
        return jsonify({"Error": "O campo nome não pode ser vazio"}), 400
    if any(char.isdigit() for char in data['nome']):
        return jsonify({"Error": "O campo nome não pode conter números."}), 400
    categoria_atual = CategoriaService.buscar_por_id(id)
    if categoria_atual is None:
        return jsonify({"Error": "Categoria não encontrada"}), 404

    # Verificar se o nome da categoria não mudou
    if categoria_atual.nome == nome:
        return jsonify({"Message": "Categoria não atualizada. O nome é o mesmo."}), 200


    try:
        response = CategoriaService.update_categoria(id, data)
        return jsonify(response), 200
    except CategoriaNaoEncontrada as cne:
        return jsonify({"error": str(cne)}), 404