from repository.fabricante_repository import FabricanteRepository
from exceptions.fabricante_existente_exception import FabricanteExistenteException
from exceptions.fabricante_nao_existente_exception import FabricanteNaoExistenteException
from exceptions.id_inexistente_exception import IdInexistenteException
from utils.functions import format_string, verify_phone_number
class FabricanteService:

    @staticmethod
    def get_by_id(id):
        '''Função para buscar um fabricante pelo id'''
        fabricante = FabricanteRepository.get_by_id(id)
        if fabricante:
            return fabricante
        raise ValueError("Fabricante não cadastrado")

    @staticmethod
    def get_by_nome(nome):
        '''Função para buscar um fabricante pelo nome'''
        fabricante = FabricanteRepository.get_by_nome(nome)
        if fabricante:
            return fabricante
        raise ValueError("Fabricante não cadastrado")
    
    @staticmethod
    def get_all():
        '''Função para buscar todos os registros de fabricante'''
        fabricantes = FabricanteRepository.get_all()
        return [fabricante.to_dict() for fabricante in fabricantes]
    
    @staticmethod
    def create(fabricante):
        '''Adicionar um fabricante'''
        fabricante_existente = FabricanteRepository.get_by_nome(fabricante.nome)
        
        if fabricante_existente:
            raise FabricanteExistenteException("Fabricante já cadastrado")
        
        return FabricanteRepository.create(fabricante)
    
    @staticmethod
    def delete_by_id(id):
        '''Função para deletar um fabricante pelo ID'''
        fabricante = FabricanteRepository.get_by_id(id)
        
        if not fabricante:
            raise FabricanteNaoExistenteException("Fabricante não encontrado para exclusão.")
        
        return FabricanteRepository.delete(fabricante)
    
    @staticmethod
    def update(id: int, fabricante_atualizado: object):
    
        if not fabricante_atualizado.nome:
            raise ValueError('Nome do fabricante não fornecido')
        elif not fabricante_atualizado.cnpj:
            raise ValueError('CNPJ não fornecido')
        elif len(fabricante_atualizado.cnpj) != 14:
            raise ValueError('CNPJ deve ter 14 dígitos')
        

        fabricante = FabricanteRepository.get_by_id(id)
        if fabricante:
            fabricante_atualizado.nome = format_string(fabricante_atualizado.nome, "Nome")
            fabricante.nome = fabricante_atualizado.nome
            fabricante.cnpj = fabricante_atualizado.cnpj
            fabricante.telefone = fabricante_atualizado.telefone
            return FabricanteRepository.update(id, fabricante)
        else:
            raise IdInexistenteException('ID não encontrado')
