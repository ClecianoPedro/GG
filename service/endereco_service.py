from repository.endereco_repository import EnderecoRepository
from entity.endereco import Endereco
from exceptions.endereco_existente_exception import EnderecoExistenteException

class EnderecoService:

    @staticmethod
    def cadastrar_endereco(endereco):
        # endereco_cep = EnderecoRepository.get_by_cep(endereco.cep)
        # if endereco_cep:
        #     raise EnderecoExistenteException("Endereço já cadastrado")
        # if len(endereco.nome) < 3:
        #     raise ValueError("Endereço menor que 3 caracteres")
        return EnderecoRepository.create(endereco)
    
    @staticmethod
    def buscar_por_id(id):
        endereco = EnderecoRepository.get_by_id(id)
        if not endereco:
            raise ValueError("Endereço não cadastrado")
        return endereco
    
    @staticmethod
    def buscar_todos():
        enderecos = EnderecoRepository.get_all()
        return [endereco.to_dict() for endereco in enderecos]
    
    @staticmethod
    def deletar_por_id(id):
        endereco = EnderecoRepository.delete(id)
        if not endereco:
            raise ValueError("Endereço não encontrado")
        
        return {"message": "Endereço deletado com sucesso!"}
    
    @staticmethod
    def update_endereco(id, data):
        endereco = EnderecoRepository.update(id, data)
        if not endereco:
            raise ValueError("Endereço não encontrado")
        
        return {"message": "Endereço atualizado com sucesso!"}