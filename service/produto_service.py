from repository.produto_repository import ProdutoRepository
from entity.produto import Produto
from exceptions.produto_exception import ProdutoExistente, ProdutoNaoEncontrado, ProdutoSemNome
from exceptions.categoria_exception import CategoriaNaoEncontrada
from repository.categoria_repository import CategoriaRepository
import psycopg2
import re
from sqlalchemy.orm import Session

def verificar_n_serie(n_serie, produto_id=None):
    if n_serie:
        # Utilize no_autoflush para evitar o envio de alterações prematuras
        session = Produto.query.session
        with session.no_autoflush:
            produto_existente = Produto.query.filter(Produto.n_serie == n_serie).first()
            if produto_existente and produto_existente.id != produto_id:
                raise ValueError(f"O número de série existente.")



class ProdutoService:

    @staticmethod
    def buscar_por_nome(nome):
        produtos = ProdutoRepository.get_by_name(nome)
        if not produtos:
            raise ProdutoNaoEncontrado('Produto não encontrado')
        return [produto.to_dict() for produto in produtos]
    
    @staticmethod
    def buscar_por_id(id):
        produto = ProdutoRepository.get_by_id(id)
        if produto:
            return produto
        raise ProdutoNaoEncontrado('Produto não encontrado')
    
    @staticmethod
    def buscar_por_n_serie(n_serie):
        produto = ProdutoRepository.get_by_serie(n_serie)
        if not produto:
            raise ValueError('Produto não existente')
        return produto
    
    @staticmethod
    def buscar_todos():
        produtos = ProdutoRepository.get_all()
        return [produto.to_dict() for produto in produtos]
    
    @staticmethod
    def cadastrar_produto(produto):
        if not ProdutoService.validar_nome(produto.nome):
            raise ProdutoSemNome('O nome do produto não pode ser composto apenas por caracteres especiais.')
        if produto.n_serie and produto.n_serie.strip() != "":
            produto_existente = ProdutoRepository.get_by_serie(produto.n_serie)
            if produto_existente:
                raise ProdutoExistente(f"O número de série {produto.n_serie} já está em uso.")
        categoria = ProdutoRepository.get_category(produto.id_categoria)
        if produto.nome == "" or produto.nome == None or produto.nome == " ":
            raise ProdutoSemNome("O produto precisa ter nome")
        if not categoria:
            raise CategoriaNaoEncontrada('Categoria não encontrada')
        return ProdutoRepository.create(produto)


    @staticmethod
    def delete(id):
        produto = ProdutoRepository.get_by_id(id)
        if produto:
            return ProdutoRepository.delete(produto)
        raise ProdutoNaoEncontrado('Produto não encontrado')

    @staticmethod
    def update_produto(id, produto_atualizado):
        if not produto_atualizado or not produto_atualizado.nome:
            raise ProdutoSemNome('O nome do produto não pode ser vazio.')

        # Verificando e normalizando o número de série
        n_serie = produto_atualizado.n_serie.strip() if produto_atualizado.n_serie else None

        if n_serie:
            try:
                verificar_n_serie(n_serie, produto_id=id)
            except ValueError as e:
                raise ProdutoExistente(str(e))

        # Obter o produto existente
        produto_existente = ProdutoRepository.get_by_id(id)
        if not produto_existente:
            raise ProdutoNaoEncontrado("Produto não encontrado para atualização.")

        # Verificar e atualizar categoria, se necessário
        nova_categoria_id = produto_atualizado.id_categoria
        if nova_categoria_id != produto_existente.id_categoria:
            categoria = CategoriaRepository.get_by_id(nova_categoria_id)
            if not categoria:
                raise CategoriaNaoEncontrada('Categoria não encontrada')

        # Atualizar o produto diretamente no repositório
        produto_atualizado = ProdutoRepository.update(
            id,
            {
                "nome": produto_atualizado.nome,
                "modelo": produto_atualizado.modelo,
                "marca": produto_atualizado.marca,
                "n_serie": produto_atualizado.n_serie,
                "id_categoria": produto_atualizado.id_categoria
            }
        )

        if not produto_atualizado:
            raise ProdutoNaoEncontrado("Erro inesperado ao atualizar o produto.")

        # Retorna o produto atualizado como dicionário
        return produto_atualizado.to_dict()
    
    def validar_nome(nome):
        # Expressão regular para verificar se o nome contém pelo menos uma letra ou número
        # ^[\w\s]*$ permite letras, números e espaços, mas não caracteres especiais
        return bool(re.search(r'[a-zA-Z0-9]', nome))


