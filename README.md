# Tasks Flask CRUD

Uma aplicação básica de gerenciamento de tarefas desenvolvida com Flask, implementando operações CRUD (Create, Read, Update, Delete).

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do curso da Rocketseat e consiste em uma API REST simples para gerenciamento de tarefas. A aplicação permite criar, listar, visualizar, atualizar e deletar tarefas através de endpoints HTTP.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Flask** - Framework web minimalista
- **Pytest** - Framework de testes
- **Requests** - Biblioteca para requisições HTTP (testes)

## 📁 Estrutura do Projeto

```
tasks_flask_crud/
├── app.py                 # Aplicação principal Flask
├── models/
│   └── task.py           # Modelo da classe Task
├── test_requests.py      # Testes automatizados
└── README.md            # Documentação do projeto
```

## 🛠️ Funcionalidades

### Operações CRUD Disponíveis:

- **CREATE**: Criar nova tarefa
- **READ**: Listar todas as tarefas ou buscar tarefa específica
- **UPDATE**: Atualizar tarefa existente
- **DELETE**: Deletar tarefa

## 📡 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST   | `/tasks` | Criar nova tarefa |
| GET    | `/tasks` | Listar todas as tarefas |
| GET    | `/tasks/<id>` | Buscar tarefa específica |
| PUT    | `/tasks/<id>` | Atualizar tarefa |
| DELETE | `/tasks/<id>` | Deletar tarefa |

### Exemplos de Uso

#### Criar Tarefa
```bash
POST /tasks
Content-Type: application/json

{
    "title": "Minha nova tarefa",
    "description": "Descrição da tarefa"
}
```

#### Listar Tarefas
```bash
GET /tasks
```

#### Buscar Tarefa Específica
```bash
GET /tasks/1
```

#### Atualizar Tarefa
```bash
PUT /tasks/1
Content-Type: application/json

{
    "title": "Tarefa atualizada",
    "description": "Nova descrição",
    "completed": true
}
```

#### Deletar Tarefa
```bash
DELETE /tasks/1
```

## ⚙️ Como Executar

### Pré-requisitos
- Python 3.x instalado
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd tasks_flask_crud
```

2. Instale as dependências:
```bash
pip install flask pytest requests
```

3. Execute a aplicação:
```bash
python app.py
```

A aplicação estará rodando em `http://127.0.0.1:5000`

## 🧪 Executando os Testes

O projeto inclui testes automatizados que validam todas as operações CRUD.

Para executar os testes:

1. Certifique-se de que a aplicação está rodando:
```bash
python app.py
```

2. Em outro terminal, execute os testes:
```bash
pytest test_requests.py -v
```

### Testes Incluídos:
- ✅ `test_create_task()` - Valida criação de tarefas
- ✅ `test_get_tasks()` - Valida listagem de tarefas
- ✅ `test_get_task()` - Valida busca de tarefa específica
- ✅ `test_update_task()` - Valida atualização de tarefas
- ✅ `test_delete_task()` - Valida deleção de tarefas

## 📝 Modelo de Dados

### Classe Task

```python
class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
```

#### Atributos:
- **id** (int): Identificador único da tarefa
- **title** (string): Título da tarefa
- **description** (string): Descrição detalhada da tarefa
- **completed** (boolean): Status de conclusão da tarefa

## 🎯 Funcionalidades Implementadas

- [x] Criação de tarefas
- [x] Listagem de todas as tarefas
- [x] Busca de tarefa por ID
- [x] Atualização de tarefas
- [x] Deleção de tarefas
- [x] Testes automatizados
- [x] Tratamento de erros (404 para tarefas não encontradas)
- [x] Contagem total de tarefas na listagem

## 🔧 Melhorias Futuras

- [ ] Implementar banco de dados (SQLite/PostgreSQL)
- [ ] Adicionar autenticação de usuários
- [ ] Implementar paginação na listagem
- [ ] Adicionar filtros e busca
- [ ] Criar interface web (frontend)
- [ ] Implementar logging
- [ ] Adicionar validações mais robustas
- [ ] Deploy em produção

## 📚 Recursos de Aprendizado

Este projeto aborda conceitos importantes como:

- Desenvolvimento de APIs REST com Flask
- Operações CRUD
- Testes automatizados com Pytest
- Estruturação de projetos Python
- Manipulação de dados JSON
- Tratamento de erros HTTP

## 📖 Documentação de Referência

- [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Requests Documentation](https://docs.python-requests.org/)

## 🤝 Contribuição

Este projeto foi desenvolvido para fins educacionais como parte do curso da Rocketseat. Sinta-se à vontade para fazer fork, sugerir melhorias ou usar como base para seus próprios projetos!

---

**Desenvolvido com ❤️ durante o curso da Rocketseat**
