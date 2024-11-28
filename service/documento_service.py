from repository.documento_repository import DocumentoRepository
import os
import uuid
from werkzeug.utils import secure_filename

class DocumentoService:

    @staticmethod
    def cadastrar_documento(documento):
        return DocumentoRepository.create(documento)
    
    @staticmethod
    def upload_file(file):
        # Atualiza o nome do arquivo para ser único e seguro
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"  # Adiciona um UUID antes do nome do arquivo

        # Define o caminho para salvar o arquivo
        caminho_save = os.path.join("static", "upload", unique_filename)
        
        # Salva o arquivo
        file.save(caminho_save)
        
        # Converte o caminho para o padrão com barras "/" antes de retornar
        caminho_save = caminho_save.replace("\\", "/")
        return caminho_save

    @staticmethod
    def buscar_por_id(id):
        documento = DocumentoRepository.get_by_id(id)
        if not documento:
            raise ValueError("Documento não encontrado")
        return documento
    
    @staticmethod
    def buscar_todos():
        documentos = DocumentoRepository.get_all()
        return [documento.to_dict() for documento in documentos]
    
    @staticmethod
    def deletar_por_id(id):
        documento = DocumentoRepository.delete(id)
        if not documento:
            raise ValueError("Documento não encontrado")
        
        return{"message": "Documento deletado com sucesso!"}
    
    @staticmethod
    def update_documento(id, data):
        documento = DocumentoRepository.update(id, data)
        if not documento:
            raise ValueError("Documento não encontrado")
        
        return {"message": "Documento atualizado com sucesso!"}