from flask import Blueprint, jsonify, request
from service.produto_service import ProdutoService
from entity.produto import Produto
from utils.functions import login_required, role_required, format_string, normalize_text
from exceptions.produto_exception import ProdutoExistente, ProdutoNaoEncontrado, ProdutoSemNome
from exceptions.categoria_exception import CategoriaNaoEncontrada
produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/<nome>', methods=['GET'])
def get_produto(nome):
    try:
        produto = ProdutoService.buscar_por_nome(nome)
        return jsonify(produto), 200
    except ProdutoNaoEncontrado as pne:
        return jsonify({"Error":str(pne)}), 404

@produto_bp.route('/<int:id>', methods=['GET'])
def get_produto_id(id):
    try:
        produto = ProdutoService.buscar_por_id(id)
        return jsonify(produto.to_dict()), 200
    except ProdutoNaoEncontrado as pne:
        return jsonify({"Error":str(pne)}), 404
    
@produto_bp.route('', methods=['GET'])
def get_produtos():
    produtos = ProdutoService.buscar_todos()
    return jsonify(produtos)

@produto_bp.route('', methods=['POST'])
def cadastrar_produto():
    data = request.get_json()

    try:
        nome = data.get('nome', '')
        modelo = data.get('modelo', '')
        marca = data.get('marca', '')
        n_serie = data.get('n_serie', '')
        id_categoria = data.get('id_categoria')

        # Validando a obrigatoriedade do campo 'nome'
        if not nome:
            return jsonify({"Error": "O campo 'nome' é obrigatório."}), 400

        # Normalizando apenas se os campos não forem vazios
        produto = Produto(
            nome=normalize_text(nome, 'nome'),
            modelo=normalize_text(modelo, 'modelo') if modelo else None, 
            marca=normalize_text(marca, 'marca') if marca else None, 
            n_serie=normalize_text(n_serie, 'n_serie') if n_serie else None,  
            id_categoria=int(id_categoria)
        )

        # Chamando o serviço para salvar o produto
        produto_salvo = ProdutoService.cadastrar_produto(produto)
        return jsonify(produto_salvo.to_dict()), 201

    except ProdutoSemNome as psn:
        return jsonify({"Error": str(psn)}), 400
    except ProdutoExistente as pe:
        return jsonify({"Error": str(pe)}), 403
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except CategoriaNaoEncontrada as cne:
        return jsonify({'Error': str(cne)}), 404
    except Exception as ex:
        return jsonify({"Error": f"Erro inesperado: {str(ex)}"}), 500
    
@produto_bp.route('/<int:id>', methods=['DELETE'])
def delete_produto(id):
    try:
        produto_deletado = ProdutoService.delete(id)
        return jsonify(produto_deletado), 200

    except ProdutoNaoEncontrado as pne:
        return jsonify({'Error': str(pne)}), 404
    except ValueError as e:
        return {'Error':str(e)}, 400
    
@produto_bp.route('/<int:id>', methods=['PUT'])
def update_produto(id):
    # Função de comparação para evitar alterações desnecessárias
    def compara_valores(valor_atual, valor_requisitado):
        if valor_atual is None:
            valor_atual = ""
        if valor_requisitado is None:
            valor_requisitado = ""
        return normalize_text(valor_requisitado.strip(), 'nome') == normalize_text(valor_atual.strip(), 'nome')

    data = request.json  # Recebe os dados da requisição

    # Buscando o produto atual no banco
    try:
        produto_atual = ProdutoService.buscar_por_id(id)
        if not produto_atual:
            return jsonify({"Error": "Produto não encontrado"}), 404
    except ProdutoNaoEncontrado:
        return jsonify({"Error": "Produto não encontrado"}), 404

    # Normalizando os campos antes de comparar ou atualizar
    nome = data.get('nome', '').strip()
    if not nome:  # Se 'nome' não foi fornecido ou está vazio, usa o nome atual
        nome = produto_atual.nome

    categoria = data.get('categoria') 

    if not categoria:
        return jsonify({"Error": "O campo 'categoria' é obrigatório e não pode ser vazio."}), 400

    # Garantir que categoria seja um inteiro
    try:
        categoria = int(categoria)
    except ValueError:
        return jsonify({"Error": "O campo 'categoria' deve ser um número inteiro válido."}), 400

    
    dados_nao_alterados = True
    # Comparando os campos com a função de comparação local
    if not compara_valores(produto_atual.nome, nome):
        dados_nao_alterados = False
    # Comparando a categoria
    categoria_atual = produto_atual.id_categoria
    categoria_requisitada = data.get('categoria')
    
    if categoria_requisitada and categoria_requisitada != str(categoria_atual):
        dados_nao_alterados = False
    # Comparando o modelo
    if not compara_valores(produto_atual.modelo, data.get('modelo', '')):
        dados_nao_alterados = False
    # Comparando a marca
    if not compara_valores(produto_atual.marca, data.get('marca', '')):
        dados_nao_alterados = False
    # Comparando o número de série
    if not compara_valores(produto_atual.n_serie, data.get('n_serie', '')):
        dados_nao_alterados = False
    # Retorna mensagem se nada foi alterado
    if dados_nao_alterados:
        return jsonify({"Message": "Nenhuma alteração foi feita no produto."}), 200

    try:
        produto_atual.nome = normalize_text(data.get('nome', produto_atual.nome), 'nome')
        produto_atual.modelo = normalize_text(data.get('modelo', produto_atual.modelo), 'modelo')
        produto_atual.marca = normalize_text(data.get('marca', produto_atual.marca), 'marca')
        produto_atual.n_serie = normalize_text(data.get('n_serie', produto_atual.n_serie), 'n_serie')
        # Garantindo que 'id_categoria' seja um número inteiro
        produto_atual.id_categoria = int(data.get('id', produto_atual.id_categoria))
        # Chamando o serviço para atualizar
        produto_atualizado = ProdutoService.update_produto(id, produto_atual)
        return jsonify(produto_atualizado), 200
    except ProdutoSemNome as psn:
        return jsonify({"Error": str(psn)}), 400
    except ProdutoExistente as pe:
        return jsonify({"Error": str(pe)}), 403
    except ProdutoNaoEncontrado as pne:
        return jsonify({"Error": str(pne)}), 404
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    except Exception as e:
        return jsonify({"Error": f"Erro inesperado: {str(e)}"}), 500
