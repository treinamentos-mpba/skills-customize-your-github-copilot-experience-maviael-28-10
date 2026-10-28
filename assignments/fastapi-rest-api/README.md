# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar um catálogo de livros com FastAPI. Você praticará rotas HTTP, validação de dados, códigos de status e operações CRUD.

## 📝 Tarefas

### 🛠️ Consultar livros pela API

#### Descrição
Use o código inicial para executar a aplicação e implemente as rotas que permitem consultar os livros do catálogo.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi uvicorn` e iniciar a API com `python starter-code.py`.
- Implementar `GET /books` para retornar todos os livros como JSON, incluindo `id`, `title` e `author`.
- Implementar `GET /books/{book_id}` para retornar um livro pelo ID ou responder com status `404` quando ele não existir.
- Retornar o livro de ID `1` neste formato:

  ```json
  {
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien"
  }
  ```

### 🛠️ Criar e atualizar livros

#### Descrição
Adicione operações para cadastrar livros e atualizar os dados de um livro existente, usando um modelo Pydantic para validar o corpo das requisições.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para criar um livro com título e autor e responder com status `201` e o livro criado.
- Gerar um ID único para cada novo livro.
- Implementar `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente.
- Responder com status `404` ao tentar atualizar um ID inexistente.

### 🛠️ Excluir livros e testar as rotas

#### Descrição
Complete as operações CRUD adicionando a exclusão de livros e verifique os endpoints pela documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /books/{book_id}` e responder com status `204` ao excluir um livro existente.
- Responder com status `404` ao tentar excluir um ID inexistente.
- Permitir testar as operações em `/docs` enquanto a aplicação estiver em execução.