from repository.loja_repository import LojaRepository
from service.endereco_service import EnderecoService
from repository.endereco_repository import EnderecoRepository
from entity.loja import Loja
from exceptions.loja_existente_exception import LojaExistenteException
from exceptions.id_inexistente_exception import IdInexistenteException

class LojaService:

    @staticmethod
    def cadastrar_loja(loja, endereco):
        
        ## Criar o Endereço -> Endereco service (Essa funcao retorna o Endereco cadastrado)
        endereco = EnderecoService.cadastrar_endereco(endereco)
        
        ## Adiciono Id Endereco em Loja
        loja.id_endereco = endereco.id
        
        ## Cadastro loja
        loja_cnpj = LojaRepository.get_by_cnpj(loja.cnpj)
        if loja_cnpj:
            raise LojaExistenteException("CNPJ já cadastrado")
        if len(loja.nome) < 3:
            raise ValueError("Nome do loja menor que 3 caracteres")

        return LojaRepository.create(loja)
    
    @staticmethod
    def buscar_por_id(id):
        loja = LojaRepository.get_by_id(id)
        if not loja:
            raise ValueError("Loja não cadastrado")
        return loja

    # @staticmethod
    # def buscar_por_cnpj(cnpj):
    #     loja = LojaRepository.get_by_cnpj(cnpj)
    #     if not loja:
    #         raise ValueError("Loja não cadastrado")
    #     return loja

    @staticmethod
    def buscar_todos():
        lojas = LojaRepository.get_all()
        return [loja.to_dict() for loja in lojas]
    
    @staticmethod
    def deletar_por_id(id):
        loja = LojaRepository.delete(id)
        if not loja:
            raise ValueError("Loja não encontrado")
        
        return True

    @staticmethod
    def update_loja(id, loja, endereco):
        loja_antiga = LojaRepository.get_by_id(id)
        if not loja_antiga:
            raise ValueError("Loja não encontrada")
        
        endereco_antigo = EnderecoRepository.get_by_id(loja_antiga.id_endereco)
        if not endereco_antigo:
            raise ValueError("Endereço não encontrado")
        
        loja.id = loja_antiga.id
        endereco.id = endereco_antigo.id

        loja = LojaRepository.update(id, loja)
        endereco = EnderecoRepository.update(loja_antiga.id_endereco, endereco)
        
        loja.id_endereco = endereco.id

        return loja