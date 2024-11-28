from app import db
import enum

class CategoriaEnum(enum.Enum):
    ELETRONICOS = "Eletrônicos"
    ELETRODOMESTICOS = "Eletrodomésticos"
    MOVEIS = "Móveis"
    INFORMATICA = "Equipamentos de Informática"
    CELULARES_SMARTPHONES = "Celulares e Smartphones"
    INSTRUMENTOS_MUSICAIS = "Instrumentos Musicais"
    CAMERAS_ACESSORIOS = "Câmeras e Acessórios"
    AR_CONDICIONADO = "Ar Condicionado e Ventiladores"
    FERRAMENTAS_MAQUINAS = "Ferramentas e Máquinas"
    ROUPAS_ACESSORIOS = "Roupas e Acessórios"
    CALCADOS = "Calçados"
    JOIAS_RELOGIOS = "Joias e Relógios"
    UTENSILIOS_DOMESTICOS = "Utensílios Domésticos"
    ACESSORIOS_AUTOMOVEIS = "Acessórios para Automóveis"
    FOTOGRAFIA = "Equipamentos de Fotografia"
    PRODUTOS_ANIMAIS = "Produtos para Animais de Estimação"
    VIDEOGAMES = "Jogos de Vídeo e Consoles"
    INSTRUMENTOS_MEDICAO = "Instrumentos de Medição e Teste"
    ARTIGOS_ESPORTIVOS = "Artigos Esportivos"
    CONSTRUCAO_REFORMA = "Materiais de Construção e Reforma"
    JARDINAGEM = "Produtos de Jardinagem"
    BELEZA_CUIDADOS = "Produtos de Beleza e Cuidados Pessoais"
    ARTIGOS_FESTA_DECORACAO = "Artigos de Festa e Decoração"
    ALIMENTOS_BEBIDAS = "Alimentos e Bebidas"
    SAUDE_BEMESTAR = "Saúde e Bem-estar"
    MOBILIARIO_COMERCIAL = "Mobiliário Comercial"
    REFRIGERACAO_AQUECIMENTO = "Equipamentos de Refrigeração e Aquecimento"
    BRINQUEDOS_JOGOS = "Brinquedos e Jogos Educativos"
    PAPELARIA = "Artigos de Papelaria"
    PRODUTOS_BEBES_CRINANCAS = "Produtos para Bebês e Crianças"
    OUTRO = "Outro"

class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.Enum(CategoriaEnum), nullable=False)  # Aqui usamos o Enum corretamente

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome.value  # Usando 'value' para acessar o nome da categoria
        }

    def to_dict_resumida(self):
        return {
            'nome': self.nome.value  # Usando 'value' para acessar o nome da categoria
        }
