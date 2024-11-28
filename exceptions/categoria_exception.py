class CategoriaExistente(Exception):
    def __init__(self, message):
        super().__init__(message)
    
class CategoriaNaoEncontrada(Exception):
    def __init__(self, message):
        super().__init__(message)

class CategoriaSemNome(Exception):
    def __init__(self, message):
        super().__init__(message)