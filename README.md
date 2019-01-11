# Let's code

Esse repositório contém todas as informações para a execução da avaliação.

Caso considere que esteja faltando alguma informação para a execução do exame, abra uma issue no repositório e ela será avaliada.

### Requisitos

A aplicação a ser desenvolvida consiste em uma lista de tarefas que suporte múltiplos usuários.

Implemente o cadastro de usuários e tarefas no banco de dados (SQLite). O formato JSON deve ser utilizado para serialização dos dados.

Devem ser implementados **testes funcionais** para todas as rotas descritas.

O usuário possui os seguintes campos e regras:

- `id`: identificador do usuário
- `name`: deve ter no máximo 50 caracteres
- `email`: validar se o formato do dado corresponde ao formato de email
- `age`: deve ser no mínimo 18 anos
- `user_type`: tipo de usuário. Opções: `admin`, `manager`, `default`

Rotas e métodos a serem implementados para os usuários:

| Rota        | Método | Ação                    |
|-------------|--------|-------------------------|
| /users      | GET    | Lista de usuários       |
| /users      | POST   | Cria usuário            |
| /users/{id} | GET    | Retorna usuário por id  |
| /users/{id} | PUT    | Atualiza usuário por id |
| /users/{id} | DELETE | Apaga usuário por id    |

A tarefa possui os seguintes campos e regras:

- `id`: identificador da tarefa
- `user_id`: identificador do usuário
- `description`: deve ter no máximo 50 caracteres

Rotas e métodos a serem implementados para os tarefas:

| Rota        | Método | Ação                   |
|-------------|--------|------------------------|
| /tasks      | GET    | Lista de tarefas       |
| /tasks      | POST   | Cria tarefa            |
| /tasks/{id} | GET    | Retorna tarefa por id  |
| /tasks/{id} | PUT    | Atualiza tarefa por id |
| /tasks/{id} | DELETE | Apaga tarefa por id    |

### Desafio

Implemente a rota para retornar as tarefas de um determinado usuário

| Rota               | Método | Ação                                 |
|--------------------|--------|--------------------------------------|
| /users/{id}/task  | GET    | Lista de tarefas do usuário por id   |

### Avaliação

Você será avaliado pelo código e testes desenvolvidos e por respeitar o guia de estilo de código [PEP8](https://www.python.org/dev/peps/pep-0008/).

Para o desenvolvimento da API e testes devem ser utilizados frameworks (Django, Flask, Pytest, etc). Podem ser usados os frameworks que você tem mais experiência.

Separe os commits por passos que foram executados para a execução do projeto em um nível adequado de detalhamento (nem muito nem pouco detalhado).

É esperado que você consiga explicar as decisões que tomou durante o desenvolvimento através de commits.

Obrigatórios:

* Python 3.x
* Testes funcionais dos endpoints (não é necessário teste unitário)
* [PEP8](https://www.python.org/dev/peps/pep-0008/)
* Mensagens de commits em inglês

### Publicando

Adicione um arquivo HOWTO.md com os procedimentos para inicialização e execução da aplicação e dos testes. Trabalhe sozinho e não compartilhe o projeto na internet.

Faça o fork esse repositório e ao finalizar abra um Pull Request com o resultado e  como as instruções para execução do projeto. Toda a comunicação referente à submissão será feita no próprio Pull Request.

## Boa sorte!