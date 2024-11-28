from functools import wraps #garante que eu não modifique os dados da requisição 'f'
from flask import request, jsonify
from string import punctuation
from email_validator import validate_email, EmailNotValidError
import jwt, re, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def login_required(f): # 'f' são todos os dados da requisição 
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization') #Pega o token enviado na requisição
        if not auth_header:
            return jsonify({'Error':'Token não enviado'}), 401
        auth_header = auth_header.replace('Bearer ', '') #Subistitui "Bearer" por espaço vazio
        payload = validate_token(auth_header) #Válida o token enviado na requisição
        if not payload:
            return jsonify({'Error':'Authentication required'}), 401
        request.user_email = payload.get('subject') #Pega o email enviado no token
        return f(*args, **kwargs)
    return decorated_function

def role_required(required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({'Error':'Authentication required'}), 401
            
            auth_header = auth_header.replace('Bearer ', '')
            payload = validate_token(auth_header)
            if not payload:
                return jsonify({'Error':'Token inválido'}), 401

            user_role = payload.get('role')
            if user_role not in required_roles:
                return jsonify({'Error':'Permissão negada'}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def validate_token(token):
    try:
        payload = jwt.decode(token, 'GGFAP', algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError('Token expirado')
    except jwt.InvalidTokenError:
        raise ValueError('Token inválido')

def validate_email_with_domain(email:str):
    """Valida o email conforme RFC 5322 e verifica se o domínio possui registro DNS."""
    def validate_local_part(string: str) -> bool:
        partes = string.split('@', 1)
        if len(partes) < 2:
            return False
        return bool(re.fullmatch(r'[a-z0-9]+(\.[a-z0-9]+)*', partes[0]))
    
    if validate_local_part(email):
        try:
            if validate_email(email, check_deliverability=True):
                return True
        except EmailNotValidError as enve:
            raise ValueError(f"E-mail inválido: {str(enve)}")
        except Exception as e:
            # Captura erros como: falha de DNS
            raise ValueError(f"Erro ao validar o e-mail: {str(e)}")

def format_string(string:str, key:str):
    '''Remove os espaços do inicio e do final, caso haja 2 ou mais espaços seguidos substitui por apenas 1 e transforma em minúsculo'''
    def replace_spaces(string):
        '''Substitui 2 ou mais espaços por apenas 1 e transforma para minusculo'''
        return re.sub(r'\s+', ' ', string).strip().lower()
    
    def has_special_characters(string:str) -> bool:
        '''Verifica se string contém caracteres especiais'''
        return any(char in punctuation for char in string)
    
    def contains_numbers(string: str) -> bool:
        '''Verifica se string contém digitos numéricos'''
        if any(char.isdigit() for char in string):
            return True
        return False
    
    if isinstance(string, str):
        if not string: #Verifica se string é vazia
            raise ValueError(f'{key} não pode ser vazia')
        elif string.isspace(): #Verifica se string contem somente espaços
            raise ValueError(f'{key} não pode conter somente espaços')
        elif contains_numbers(string):
            raise ValueError(f'{key} não pode conter números')
        elif has_special_characters(string):
            raise ValueError(f'{key} não pode conter caracteres especiais')
        string = replace_spaces(string)
        return string
    raise AttributeError(f'{key}: Valor deve ser do tipo string')

def verify_phone_number(phone_number:str, key:str):
    '''Remove os espaços, verifica se é vazio, se contém somente espaços, se contém caracteres especiais ou letras'''
    def replace_spaces(string:str):
        '''Substitui espaços por ''.'''
        return re.sub(r'\s', '', string)
    
    def has_special_characters(string:str) -> bool:
        '''Verifica se string contém caracteres especiais'''
        return any(char in punctuation for char in string)
    
    def contains_letters(string: str) -> bool:
        '''Verifica se a string contém letras'''
        return any(char.isalpha() for char in string)
    
    if isinstance(phone_number, str):
        if not phone_number:
            raise ValueError(f'{key} não pode ser vazio')
        elif phone_number.isspace():
            raise ValueError(f'{key} não pode conter somente espaços')
        elif len(phone_number) != 11:
            raise ValueError('Telefone deve conter 11 caracteres, exemplo: 66988887777')
        elif has_special_characters(phone_number):
            raise ValueError(f'{key} não pode conter caracteres especiais')
        elif contains_letters(phone_number):
            raise ValueError(f'{key} não pode conter letras')
        phone_number = replace_spaces(phone_number)
        return phone_number
    raise AttributeError(f'{key}: Valor deve ser do tipo string')

def send_recovery_code_to_mail(codigo:str, email_destino:str):
        email_origem = 'gestaodegarantiafap@gmail.com'
        senha = 'nchm ucue bbas osck'
        msg = MIMEMultipart()
        msg['From'] = email_origem
        msg['To'] = email_destino
        msg['Subject'] = 'Código de recuperação de senha'
        mensagem = f'Seu código de recuperação de senha é: {codigo}'
        msg.attach(MIMEText(mensagem, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
            servidor.starttls()
            servidor.login(email_origem, senha)
            servidor.send_message(msg)
            servidor.close()
     
def normalize_text(string: str, key: str) -> str:
    if string is None or string.strip() == "":
        return None  # Retorna None se a string for vazia ou apenas espaços

    # Remover espaços extras
    string = re.sub(r'\s+', ' ', string).strip()

    # Definir os caracteres especiais permitidos
    allowed_specials = "-_@."
    
    # Contar os caracteres especiais encontrados
    special_count = {char: string.count(char) for char in allowed_specials}

    # Verificar se algum caractere especial aparece mais de uma vez
    for char, count in special_count.items():
        if count > 1:
            raise ValueError(f"{key} pode ter no máximo um caractere especial {char}.")

    # Remover caracteres especiais indesejados, mas permitir os específicos
    allowed_chars = f"a-zA-Z0-9{re.escape(allowed_specials)}"  # Permitir letras, números e os caracteres especiais definidos
    regex_pattern = f"[^({allowed_chars})]"  # Apenas os caracteres permitidos
    string = re.sub(regex_pattern, "", string)

    # Se a string estiver vazia após a remoção, retornamos None ou levantamos um erro
    if not string:
        raise ValueError(f"{key} não pode ser vazio ou conter apenas caracteres especiais.")

    return string.lower()
