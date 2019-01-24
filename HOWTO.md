## Exemplo md

#### Pré requisitos:
- Python 3.6
- virtualenv (https://pypi.org/project/virtualenv/)

### 1. Crie o ambiente virtual dentro da pasta raíz do projeto
```
$ virtualenv -p python3.6 venv
```

### 2. Ative o ambiente virtual 
```
$ source venv/bin/activate
```

### 3. Instale as dependências do projeto
```
$ pip install -r requirements.txt
```

### 4. Configuração do Django

#### 4.1. Entre na pasta tasklists/
```
$ cd tasklist/
```

#### 4.3. Verifique se todas as migrations do Django foram criadas
```
$ ./manage.py makemigrations
```

#### 4.3. Execute as migrations do Django
```
$ ./manage.py migrate
```

### 5. Execute o server do Django
```
$ ./manage.py runserver
```

### 6. Com o ambiente virtual ativado, execute os testes
```
$ pytest
```