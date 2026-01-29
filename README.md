# Hacker Store

Uma API REST simples para gerenciar produtos de uma loja hacker, construída com Flask e SQLAlchemy.

## Funcionalidades

- Listar todos os produtos
- Criar um novo produto
- Atualizar um produto existente
- Deletar um produto

## Instalação

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd hackerstore
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```
   python run.py
   ```

A aplicação será executada em http://localhost:5000

## Uso

A API fornece os seguintes endpoints:

- **GET /produtos**: Lista todos os produtos
- **POST /produtos**: Cria um novo produto (requer JSON com `nome`, `preco`, `qtde`)
- **PUT /produtos/<id>**: Atualiza um produto existente
- **DELETE /produtos/<id>**: Deleta um produto

### Exemplos de Uso

#### Criar um produto:
```bash
curl -X POST http://localhost:5000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Produto Exemplo", "preco": 100, "qtde": 10}'
```

#### Listar produtos:
```bash
curl http://localhost:5000/produtos
```

## Tecnologias

- Flask 3.1.2
- SQLAlchemy 2.0.46
- SQLite (banco de dados)
- Colorama 0.4.6

## Estrutura do Projeto

- `app/`: Código da aplicação
  - `__init__.py`: Inicialização da aplicação Flask
  - `database.py`: Configuração do banco de dados
  - `models.py`: Modelos de dados (Produto)
  - `routes.py`: Rotas da API
- `run.py`: Ponto de entrada da aplicação
- `requirements.txt`: Dependências do Python
- `.gitignore`: Arquivos ignorados pelo Git

## Modelo de Dados

### Produto
- `id`: String (UUID) - Chave primária
- `nome`: String - Nome do produto
- `preco`: Integer - Preço do produto
- `qtde`: Integer - Quantidade em estoque
