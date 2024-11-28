from entity.produto import Produto
from entity.categoria import Categoria
from exceptions.produto_exception import ProdutoNaoEncontrado
from db import db

class ProdutoRepository:

    @staticmethod
    def get_all():
        return Produto.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Produto.query.get(id)
    
    @staticmethod
    def get_by_name(nome):
        return Produto.query.filter_by(nome=nome).all()
    
    @staticmethod
    def get_category(id):
        return Categoria.query.get(id)
    
    @staticmethod
    def get_by_serie(n_serie):
        return Produto.query.filter_by(n_serie=n_serie).first()

    
    @staticmethod
    def get_by_model(modelo):
        return Produto.query.filter_by(modelo=modelo).first()
    
    @staticmethod
    def get_by_make(marca):
        return Produto.query.filter_by(marca=marca)
    
    @staticmethod
    def create(produto):
        try:
            db.session.add(produto)
            db.session.commit()
            return produto
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def delete(produto):
        try:
            db.session.delete(produto)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update(id, produto_data):
        try:
            # Busca o produto no banco
            produto = Produto.query.get(id)
            if not produto:
                raise ProdutoNaoEncontrado(f'Produto com id {id} não encontrado.')  # Retorna None se o produto não for encontrado
            
            # Atualiza os campos do produto com os dados recebidos
            produto.nome = produto_data.get('nome', produto.nome)
            produto.modelo = produto_data.get('modelo', produto.modelo)
            produto.marca = produto_data.get('marca', produto.marca)
            produto.n_serie = produto_data.get('n_serie', produto.n_serie)
            produto.id_categoria = produto_data.get('id_categoria', produto.id_categoria)
            
            # Commit das mudanças
            db.session.commit()
            return produto
        except Exception as e:
            db.session.rollback()  # Reverte a transação em caso de erro
            raise e
