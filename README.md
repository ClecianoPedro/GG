<h1 align="center" style="font-weight: bold;">Gestão de Garantia 💻</h1>

<p align="center">
 <a href="#technologies">Technologies</a> • 
 <a href="#started">Getting Started</a> • 
  <a href="#routes">Endpoints</a> •
 <a href="#contribute">Collaborators</a> 
</p>

<p align="center">
    <b>GG é uma proposta de aplicação desenvolvida por alunos da Softex Pernambuco, do curso Formação Acelerada em Programação na trilha de Backend com Python. Tem como finalidade oferecer um sistema de Gestão de Garantias. O sistema deve permitir basicamente aos usuários criar conta, fazer login, recuperar a senha por envio de código ao email cadastrado, alterar a senha cadastrada previamente, fazer upload de documentos, visualizar todas as suas garantias salvas no sistema e também permitir exclui-las. </b>
</p>

<h2 id="technologies">💻 Technologies</h2>

- Python
- Flask
- PostgreSQL

<h2 id="documentation">📖 Documentation</h2>

- [Documentação do projeto](https://docs.google.com/document/d/1gf9Zn8sOwtrccqKjaQtCxWS8vb8HUTeg/edit?usp=sharing&ouid=108003084150608026515&rtpof=true&sd=true)

<h2 id="started">🚀 Getting started</h2>

<h3>Prerequisites</h3>

- [Python 3.12.7](https://www.python.org/downloads/)
- [Flask 3.0.3](https://flask.palletsprojects.com/en/stable/installation/)
- [Anaconda Navigator](https://www.anaconda.com/download)
- [PostgreSQL](https://www.postgresql.org/download/)

<h3>Cloning</h3>

How to clone the project

## **1. Clonar o Repositório**
Clone o repositório do projeto usando o comando:
```bash
git clone https://github.com/softexrecifepe/PI-SOFTEX-TURMA-15.1.git
```
---

## **2. Criar um Ambiente Virtual**
Para isolar as dependências do projeto, crie um ambiente virtual com python 3.12.7, utilizamos o Anaconda Navigator.
```bash
conda create --name nome_do_ambiente python=3.12.7
```

---

## **3. Instalar as Dependências**
Com o arquivo requirements.txt no repositório, instale as dependências com:
```bash
pip install -r requirements.txt
```

<h3>Starting</h3>

How to start your project

```bash
flask run
```

<h2 id="routes">📍 API Endpoints</h2>

| Route                                   | Description               |
|-----------------------------------------|---------------------------|
| `POST /auth/login`                      | Login do usuário.         |
| `POST /auth/register`                   | Cadastrar usuário.        |
| `POST /auth/register/admin`             | Cadastrar usuário admin.  |
| `GET /auth/usuario/<ID>`                | Buscar usuário por ID.    |
| `POST /auth/password_recovery`          | Recuperar senha.          |
| `POST /auth/reset_password`             | Alterar senha via código. |
| `GET  /usuario`                         | Buscar todos usuários.    |
| `PUT  /usuario/<ID>`                    | Atualizar usuário.        |
| `PUT  /usuario/<ID>/change_password`    | Atualizar senha.          |
| `DELETE  /usuario/<ID>`                 | Deletar usuário.          |
| `POST  /fabricante`                     | Cadastrar fabricante.     |
| `GET /fabricante`                       | Buscar todos fabricantes. |
| `GET /fabricante/<USER_ID>/<ID>`        | Buscar fabricantes por id.|
| `PUT /fabricante/<USER_ID>/<ID>`        | Atualizar fabricante.     |
| `DELETE /fabricante/<USER_ID>/<ID>`     | Deletar um fabricante.    |
| `POST /categoria`                       | Criar uma nova categoria. |
| `GET /categoria/<ID>`                   | Buscar uma categoria pelo ID. |
| `DELETE /categoria/<ID>`                | Deletar uma categoria pelo ID. |
| `POST /documento/upload`                | Fazer o upload de um documento. |
| `POST /documento`                       | Criar um novo documento. |
| `GET /documento`                        | Buscar todos os documentos. |
| `PUT /documento/<USER_ID>/<ID>`         | Atualizar um documento pelo ID. |
| `DELETE /documento/<USER_ID>/<ID>`      | Deletar um documento pelo ID. |
| `POST /loja`                            | Criar uma nova loja. |
| `GET /loja`                             | Buscar todas as lojas. |
| `PUT /loja/<ID_USER>/<ID>`              | Atualizar uma loja pelo ID. |
| `DELETE /loja/<ID_USER>/<ID>`           | Deletar uma loja pelo ID. |
| `POST /produto/<ID_USER>`               | Criar um novo produto. |
| `GET /produto`                          | Buscar todos os produtos. |
| `PUT /produto/<ID_USER>`                | Atualizar um produto pelo ID. |
| `DELETE /produto/<ID_USER>`             | Deletar um produto pelo ID. |
| `POST /garantia`                        | Criar uma nova garantia. |
| `GET /garantia`                         | Buscar todas as garantias. |
| `GET /garantia/<ID_USER>/<ID>`          | Buscar garantias por id. |
| `PUT /garantia/<ID>`                    | Atualizar garantia por ID. |
| `DELETE /garantia/<ID>`                 | Deletar garantia por ID. |
| `POST /garantia_estendida`              | Criar uma garantia estendida. |
| `GET /garantia_estendida/<ID>`          | Buscar garantia estendida por ID. |
| `PUT /garantia_estendida/<ID>`          | Atualizar garantia estendida por ID. |
| `DELETE /garantia_estendida/<ID>`       | Deletar garantia estendida por ID. |

<h3 id="get-auth-detail">POST /auth/login</h3>

**REQUEST**
```json
{
    "email": "itz@gmail.com",
    "senha": "12345678"
}
```
**RESPONSE**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
<h3 id="post-auth-detail">POST /auth/register</h3>

**REQUEST**
```json
{
    "nome": "pedro",
    "email": "itz@gmail.com",
    "senha": "12345678",
    "sexo": "masculino",
    "telefone": ""
}
```

**RESPONSE**
```json
{
    "email": "itz@gmail.com",
    "garantias": [],
    "id": 2,
    "nome": "pedro",
    "sexo": "masculino",
    "telefone": null
}
```
<h3 id="post-auth-detail">POST /auth/register/admin</h3>

**REQUEST**
```json
{
    "nome": "pedroadmin",
    "email": "itz@gmail.com",
    "senha": "12345678",
    "sexo": "masculino",
    "telefone": "81998887766"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "email": "itz@gmail.com",
    "garantias": [],
    "id": 3,
    "nome": "pedroadmin",
    "sexo": "masculino",
    "telefone": "81998887766"
} 
```
<h3 id="post-auth-detail">GET /auth/usuario/&lt;id&gt;</h3>

**RESPONSE**
```json
{
    "usuario": {
    "email": "itz@gmail.com",
    "garantias": []
    "nome": "pedro",
     "sexo": "masculino",
     "telefone": null
}
```
<h3 id="get-auth-detail">POST /auth/password_recovery</h3>

**REQUEST**
```json
{
    "email": "itz@gmail.com"
}
```
**RESPONSE**
```json
{
    "Send Email": true
}
```
<h3 id="get-auth-detail">POST /auth/reset_password</h3>

**REQUEST**
```json
{
    "email": "itz@gmail.com",
    "codigo": "867412",
    "nova_senha": "123456789"
}
```
**RESPONSE**
```json
{
    "Senha alterada": true
}
```
<h3 id="get-auth-detail">GET /usuario</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "email": "itz@gmail.com",
    "garantias": [],
    "id": 3,
    "nome": "pedroadmin",
    "sexo": "masculino",
    "telefone": "81998887766"
}
```
<h3 id="get-auth-detail">PUT /usuario/&lt;id&gt;</h3>

**REQUEST**
```json
{
    "nome": "pedro",
    "email": "itz@gmail.com",
    "sexo": "masculino",
    "telefone": "81993405000"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "email": "itz@gmail.com",
    "nome": "pedro",
    "sexo": "masculino",
    "telefone": "81993405000"
}
```
<h3 id="get-auth-detail">PUT /usuario/&lt;id&gt;/change_password</h3>

**REQUEST**
```json
{
    "senha_antiga": "12345678",
    "senha_nova": "123456789"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "Senha alterada": true
}
```
<h3 id="get-auth-detail">DELETE /usuario/&lt;id&gt;</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "Delete": true
}
```
<h3 id="get-auth-detail">POST /fabricante</h3>

**REQUEST**
```json
{
    "nome": "SAMSUNG",
    "cnpj": "12345678900011",
    "telefone": "81988887777"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "cnpj": "12345678900011",
    "id_fabricante": 1,
    "nome": "samsung",
    "telefone": "81988887777"
}
```
<h3 id="get-auth-detail">GET /fabricante</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
[
    {
        "cnpj": "12345678900011",
        "id_fabricante": 1,
        "nome": "joaovitor",
        "telefone": "81988887777"
    },
    {
        "cnpj": "12345678900011",
        "id_fabricante": 2,
        "nome": "samsung",
        "telefone": "81988887777"
    }
]
```

<h3 id="get-auth-detail">GET /fabricante/&lt;USER_ID&gt;/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "cnpj": "12345678900011",
    "id_fabricante": 1,
    "nome": "samsung",
    "telefone": "81988887777"
}
```
<h3 id="get-auth-detail">PUT /fabricante/&lt;USER_ID&gt;/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "cnpj": "12345678900012",
    "nome": "joaovitor",
    "telefone": "81988887776"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "cnpj": "12345678900012",
    "id_fabricante": 1,
    "nome": "joaovitor",
    "telefone": "81988887771"
}
```
<h3 id="get-auth-detail">DELETE /fabricante/&lt;USER_ID&gt;/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "message": true
}
```
<h3 id="get-auth-detail">POST /categoria</h3>

**REQUEST**  
```json
{
    "nome": "eletrodomesticos"
}
```

**RESPONSE**  
```json
{
    "id": 1,
    "nome": "ELETRODOMESTICOS"
}
```
<h3 id="get-auth-detail">GET /categoria/&lt;ID&gt;</h3>

**RESPONSE**  
```json
{
    "id": 1,
    "nome": "ELETRODOMESTICOS"
}
```
<h3 id="get-auth-detail">DELETE /categoria/&lt;ID&gt;</h3>

**RESPONSE**  
```json
{
    "Delete": true
}
```

<h3 id="get-auth-detail">POST /documento/upload</h3>

**RESPONSE**  
```json
{
    "Caminho": "static/upload/72b0039a-631c-4d73-b848-f5881b972de5_01.06.18_7de35f05.jpg"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
<h3 id="get-auth-detail">POST /documento</h3>

**REQUEST**  
```json
{
    "descricao": "garantia",
    "url": "static/upload/72b0039a-631c-4d73-b848-f5881b972de5_01.06.18_7de35f05.jpg"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
{
    "descricao": "garantia",
    "id": 1,
    "url": "static/upload/72b0039a-631c-4d73-b848-f5881b972de5_01.06.18_7de35f05.jpg"
}
```

<h3 id="get-auth-detail">GET /documento</h3>

**RESPONSE**  
```json
[
    {
        "descricao": "garantia",
        "id": 1,
        "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
    },
    {
        "descricao": "garantia",
        "id": 2,
        "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
    }
]
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
<h3 id="get-auth-detail">PUT /documento/&lt;USER_ID&gt;/&lt;ID&gt;</h3>

**REQUEST**  
```json
{
    "descricao": "garantia",
    "url": "static/upload/72b0039a-631c-4d73-b848-f5881b972de5_01.06.18_7de35f06.jpg"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
{
    "message": "Documento atualizado com sucesso!"
}
```

<h3 id="get-auth-detail">DELETE /documento/&lt;USER_ID&gt;/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
{
    "message": "Documento deletado com sucesso!"
}
```

<h3 id="get-auth-detail">POST /loja</h3>

**REQUEST**  
```json
{
    "nome": "exemplo",
    "cnpj": "12345678900012",
    "telefone": "81988887777",
    "url": "",
    "endereco": {
        "logradouro": "rua exemplo",
        "bairro": "exemplo",
        "numero": "500",
        "cep": "55190690",
        "cidade": "exemplo",
        "estado": "pe"
    }
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
{
    "cnpj": "12345678900012",
    "endereco": {
        "bairro": "exemplo",
        "cep": "55190690",
        "cidade": "exemplo",
        "estado": "pe",
        "id": 1,
        "logradouro": "rua exemplo",
        "numero": "500"
    },
    "id": 1,
    "nome": "exemplo",
    "telefone": "81988887777",
    "url": null
}
```

<h3 id="get-auth-detail">GET /loja</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```

**RESPONSE**  
```json
[
    {
        "cnpj": "12345678900012",
        "endereco": {
            "bairro": "exemplo",
            "cep": "55190690",
            "cidade": "exemplo",
            "estado": "pe",
            "id": 1,
            "logradouro": "rua exemplo",
            "numero": "500"
        },
        "id": 1,
        "nome": "exemplo",
        "telefone": "81988887777",
        "url": null
    }
]
```

<h3 id="get-auth-detail">PUT /loja/&lt;USER_ID&gt;/&lt;ID&gt;</h3>

**REQUEST**  
```json
{
    "nome": "exemplo1234",
    "cnpj": "12345678900016",
    "telefone": "81988889999",
    "endereco": {
        "logradouro": "exemplo5",
        "bairro": "centro",
        "numero": "825",
        "cep": "55190799",
        "cidade": "olinda",
        "estado": "pe"
    }
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
{
    "cnpj": "12345678900016",
    "endereco": {
        "bairro": "centro",
        "cep": "55190799",
        "cidade": "olinda",
        "estado": "pe",
        "id": 1,
        "logradouro": "exemplo5",
        "numero": "825"
    },
    "id": 1,
    "nome": "exemplo1234",
    "telefone": "81988889999",
    "url": null
}
```

<h3 id="get-auth-detail">DELETE /loja/&lt;USER_ID&gt;/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
{
    "message": "Loja deletada com sucesso"
}
```

<h3 id="get-auth-detail">POST /produto/&lt;ID&gt;</h3>

**REQUEST**  
```json
{
    "id_categoria": 1,
    "nome": "geladeira",
    "modelo": "",
    "marca": "",
    "n_serie": ""
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
{
    "categoria": "CALCADOS",
    "id_produto": 1,
    "marca": null,
    "modelo": null,
    "n_serie": null,
    "nome": "geladeira"
}
```

<h3 id="get-auth-detail">GET /produto</h3>

**RESPONSE**  
```json
[
    {
        "categoria": "CALCADOS",
        "id_produto": 1,
        "marca": null,
        "modelo": null,
        "n_serie": null,
        "nome": "geladeira"
    }
]
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
<h3 id="get-auth-detail">PUT /produto/&lt;ID&gt;</h3>

**REQUEST**  
```json
{
    "categoria": 1,
    "nome": "sandalia",
    "modelo": "exemplo",
    "marca": "havaianas",
    "n_serie": ""
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
{
    "categoria": "CALCADOS",
    "id_produto": 1,
    "marca": "havaianas",
    "modelo": "exemplo",
    "n_serie": null,
    "nome": "sandalia"
}
```

<h3 id="get-auth-detail">DELETE /produto/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
true
```
<h3 id="get-auth-detail">POST /garantia</h3>

**REQUEST**  
```json
{
    "id_usuario": 1,
    "id_produto": 1,
    "id_loja": 1,
    "id_documento": 1,
    "apelido": "exemplo",
    "data_inicio": "05/08/2000",
    "data_fim": "08/09/2000"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```

**RESPONSE**  
```json
{
    "apelido": "exemplo",
    "ativo": true,
    "data_fim": "08/09/2000",
    "data_inicio": "05/08/2000",
    "documento": {
        "descricao": "garantia",
        "id": 1,
        "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
    },
    "id_garantia": 1,
    "loja": {
        "cnpj": "12345678900012",
        "endereco": {
            "bairro": "exemplo",
            "cep": "55190690",
            "cidade": "exemplo",
            "estado": "pe",
            "id": 1,
            "logradouro": "rua exemplo",
            "numero": "500"
        },
        "id": 1,
        "nome": "exemplo",
        "telefone": "81988887777",
        "url": null
    },
    "produto": {
        "categoria": "CALCADOS",
        "id_produto": 1,
        "marca": null,
        "modelo": null,
        "n_serie": null,
        "nome": "geladeira"
    },
    "usuario": {
        "email": "itz@gmail.com",
        "nome": "pedro",
        "sexo": "masculino",
        "telefone": "81993405000"
    }
}
``` 

<h3 id="get-auth-detail">GET /garantia</h3>

**REQUEST**  
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```

**RESPONSE**  
```json
[
    {
        "apelido": "exemplo",
        "ativo": true,
        "data_fim": "08/09/2000",
        "data_inicio": "05/08/2000",
        "documento": {
            "descricao": "garantia",
            "id": 1,
            "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
        },
        "id_garantia": 1,
        "loja": {
            "cnpj": "12345678900012",
            "endereco": {
                "bairro": "exemplo",
                "cep": "55190690",
                "cidade": "exemplo",
                "estado": "pe",
                "id": 1,
                "logradouro": "rua exemplo",
                "numero": "500"
            },
            "id": 1,
            "nome": "exemplo",
            "telefone": "81988887777",
            "url": null
        },
        "produto": {
            "categoria": "CALCADOS",
            "id_produto": 1,
            "marca": null,
            "modelo": null,
            "n_serie": null,
            "nome": "geladeira"
        },
        "usuario": {
            "email": "itzcleciano@gmail.com",
            "nome": "pedro",
            "sexo": "masculino",
            "telefone": "81993405000"
        }
    }
]
```
<h3 id="get-auth-detail">GET /garantia/&lt;ID_USER&gt;/&lt;ID&gt;</h3>

**REQUEST**  
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**  
```json
[
    {
        "apelido": "exemplo",
        "ativo": true,
        "data_fim": "08/09/2000",
        "data_inicio": "05/08/2000",
        "documento": {
            "descricao": "garantia",
            "id": 1,
            "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
        },
        "id_garantia": 1,
        "loja": {
            "cnpj": "12345678900012",
            "endereco": {
                "bairro": "exemplo",
                "cep": "55190690",
                "cidade": "exemplo",
                "estado": "pe",
                "id": 1,
                "logradouro": "rua exemplo",
                "numero": "500"
            },
            "id": 1,
            "nome": "exemplo",
            "telefone": "81988887777",
            "url": null
        },
        "produto": {
            "categoria": "CALCADOS",
            "id_produto": 1,
            "marca": null,
            "modelo": null,
            "n_serie": null,
            "nome": "geladeira"
        },
        "usuario": {
            "email": "itzcleciano@gmail.com",
            "nome": "pedro",
            "sexo": "masculino",
            "telefone": "81993405000"
        }
    }
]
```

<h3 id="get-auth-detail">PUT /garantia/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "apelido": "EXEMPLO",
    "data_inicio": "03/10/2002",
    "data_fim": "05/11/2008",
    "ativo": false
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```

**RESPONSE**
```json
{
    "apelido": "EXEMPLO",
    "ativo": false,
    "data_fim": "05/11/2008",
    "data_inicio": "03/10/2002",
    "documento": {
        "descricao": "garantia",
        "id": 1,
        "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
    },
    "id_garantia": 1,
    "loja": {
        "cnpj": "12345678900012",
        "endereco": {
            "bairro": "exemplo",
            "cep": "55190690",
            "cidade": "exemplo",
            "estado": "pe",
            "id": 1,
            "logradouro": "rua exemplo",
            "numero": "500"
        },
        "id": 1,
        "nome": "exemplo",
        "telefone": "81988887777",
        "url": null
    },
    "produto": {
        "categoria": "CALCADOS",
        "id_produto": 1,
        "marca": null,
        "modelo": null,
        "n_serie": null,
        "nome": "geladeira"
    },
    "usuario": {
        "email": "itzcleciano@gmail.com",
        "nome": "pedro",
        "sexo": "masculino",
        "telefone": "81993405000"
    }
}
```

<h3 id="get-auth-detail">DELETE /garantia/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```

**RESPONSE**
```json
{
    "Delete": true
}
```

<h3 id="get-auth-detail">POST /garantia_estendida</h3>

**REQUEST**
```json
{
    "id_garantia": 1,
    "data_inicio": "05/08/2002",
    "data_fim": "08/09/2004"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```

**RESPONSE**
```json
{
    "ativo": true,
    "data_fim": "08/09/2004",
    "data_inicio": "05/08/2002",
    "garantia": {
        "apelido": "exemplo",
        "ativo": true,
        "data_fim": "08/09/2000",
        "data_inicio": "05/08/2000",
        "documento": {
            "descricao": "garantia",
            "id": 1,
            "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
        },
        "id_garantia": 1,
        "loja": {
            "cnpj": "12345678900012",
            "endereco": {
                "bairro": "exemplo",
                "cep": "55190690",
                "cidade": "exemplo",
                "estado": "pe",
                "id": 1,
                "logradouro": "rua exemplo",
                "numero": "500"
            },
            "id": 1,
            "nome": "exemplo",
            "telefone": "81988887777",
            "url": null
        },
        "produto": {
            "categoria": "CALCADOS",
            "id_produto": 1,
            "marca": null,
            "modelo": null,
            "n_serie": null,
            "nome": "geladeira"
        },
        "usuario": {
            "email": "itzcleciano@gmail.com",
            "nome": "pedro",
            "sexo": "masculino",
            "telefone": "81993405000"
        }
    },
    "id_garantia_estendida": 1
}
```

<h3 id="get-auth-detail">GET /garantia_estendida/<ID></h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "ativo": true,
    "data_fim": "08/09/2004",
    "data_inicio": "05/08/2002",
    "garantia": {
        "apelido": "exemplo",
        "ativo": true,
        "data_fim": "08/09/2000",
        "data_inicio": "05/08/2000",
        "documento": {
            "descricao": "garantia",
            "id": 1,
            "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
        },
        "id_garantia": 1,
        "loja": {
            "cnpj": "12345678900012",
            "endereco": {
                "bairro": "exemplo",
                "cep": "55190690",
                "cidade": "exemplo",
                "estado": "pe",
                "id": 1,
                "logradouro": "rua exemplo",
                "numero": "500"
            },
            "id": 1,
            "nome": "exemplo",
            "telefone": "81988887777",
            "url": null
        },
        "produto": {
            "categoria": "CALCADOS",
            "id_produto": 1,
            "marca": null,
            "modelo": null,
            "n_serie": null,
            "nome": "geladeira"
        },
        "usuario": {
            "email": "itzcleciano@gmail.com",
            "nome": "pedro",
            "sexo": "masculino",
            "telefone": "81993405000"
        }
    },
    "id_garantia_estendida": 1
}
```

<h3 id="put-auth-detail">PUT /garantia_estendida/<ID></h3>

**REQUEST**
```json
{
    "ativo": false,
    "data_inicio": "05/08/2002",
    "data_fim": "08/09/2005"
}
```
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "ativo": false,
    "data_fim": "08/09/2005",
    "data_inicio": "05/08/2002",
    "garantia": {
        "apelido": "exemplo",
        "ativo": true,
        "data_fim": "08/09/2000",
        "data_inicio": "05/08/2000",
        "documento": {
            "descricao": "garantia",
            "id": 1,
            "url": "static/upload/e937fc5d-3484-45e6-a1b4-6fbf96a41ac6_01.06.18_7de35f05.jpg"
        },
        "id_garantia": 1,
        "loja": {
            "cnpj": "12345678900012",
            "endereco": {
                "bairro": "exemplo",
                "cep": "55190690",
                "cidade": "exemplo",
                "estado": "pe",
                "id": 1,
                "logradouro": "rua exemplo",
                "numero": "500"
            },
            "id": 1,
            "nome": "exemplo",
            "telefone": "81988887777",
            "url": null
        },
        "produto": {
            "categoria": "CALCADOS",
            "id_produto": 1,
            "marca": null,
            "modelo": null,
            "n_serie": null,
            "nome": "geladeira"
        },
        "usuario": {
            "email": "itzcleciano@gmail.com",
            "nome": "pedro",
            "sexo": "masculino",
            "telefone": "81993405000"
        }
    },
    "id_garantia_estendida": 1
}
```
<h3 id="get-auth-detail">DELETE /garantia_estendida/&lt;ID&gt;</h3>

**REQUEST**
```json
{
    "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0IjoiaXR6QGdtYWlsLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ3NDk2M30.LDuvtWNZluVWbd8qhEafz0oNaO3mLW3-cHOh8gUUQgU"
}
```
**RESPONSE**
```json
{
    "Delete": true
}
```
<h2 id="contribute">📫 Contribute</h2>

Special thank you to all the people who contributed to this project.

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/JoaoVChaves">João Vitor Chaves</a>
    </td>
    <td align="center">
      <a href="https://github.com/ClecianoPedro">Cleciano Pedro</a>
    </td>
    <td align="center">
      <a href="https://github.com/BiriBerto">Luiz Humberto</a>
    </td>
    <td align="center">
      <a href="https://github.com/humbertojr85">Humberto Alcântara</a>
    </td>
  </tr>
</table>
