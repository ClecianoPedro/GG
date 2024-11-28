class ProdutoExistente(Exception):
    def __init__(self, message):
        super().__init__(message)

class ProdutoNaoEncontrado(Exception):
    def __init__(self, message):
        super().__init__(message)

class ProdutoSemNome(Exception):
    def __init__(self, message):
        super().__init__(message)