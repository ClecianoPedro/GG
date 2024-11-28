from repository.categoria_repository import CategoriaRepository
from entity.categoria import Categoria
from exceptions.categoria_exception import CategoriaExistente, CategoriaNaoEncontrada, CategoriaSemNome
from utils.functions import format_string

class CategoriaService:

    @staticmethod
    def buscar_por_nome(nome):
        categoria = CategoriaRepository.get_by_name(nome)
        if not categoria:
            raise CategoriaNaoEncontrada('Categoria não encontrada')
        return categoria
    
    @staticmethod
    def buscar_por_id(id):
        categoria = CategoriaRepository.get_by_id(id)
        if not categoria:
            raise CategoriaNaoEncontrada('Categoria não encontrada')
        return categoria
    
    @staticmethod
    def buscar_todas():
        categoria = CategoriaRepository.get_all()
        return [categoria.to_dict() for categoria in categoria]
    
    @staticmethod
    def cadastrar_categoria(categoria):
        
        categoria_nome = CategoriaRepository.get_by_name(categoria.nome)
        if categoria_nome:
            raise CategoriaExistente("Categoria já cadastrada")
        
        return CategoriaRepository.create(categoria)
    
    @staticmethod
    def delete(id):
        categoria = CategoriaRepository.get_by_id(id)
        if categoria:
            return CategoriaRepository.delete(categoria)
        raise CategoriaNaoEncontrada('Categoria não encontrada')
    
    @staticmethod
    def update_categoria(id, data):
        categoria = CategoriaRepository.update(id, data)
        if not categoria:
            raise CategoriaNaoEncontrada('Categoria não encontrada')
            
        return categoria.to_dict()
