# Employee Manager

## Dependências
Todos os commandos abaixo são executados utilizandos pacotes Python 3.5.

Instale as dependências listadas no arquivo requirements.txt:

```
pip install -r requirements.txt
```
## Configuração

Após a instalação das dependências, execute os comandos abaixo no diretório raiz para a criação do banco de dados e load (opcional) da carga inicial de dados (departamentos e funcionários):

```
python manage.py migrate
python manage.py loaddata departments
python manage.py loaddata employees
```

## Inicialize o servidor built-in:
```
python manage.py runserver
```
## Exemplos de Requisições

### Lista funcionários

```
GET /employee/
```
### Adiciona novo funcionário

```
POST /employee/
```

Body

```json
{
    "name": "Foo Bar",
    "email": "foo@bar.com",
    "department": "Mobile"
}
```

### Exibe detalhes de um funcionário

```
GET /employee/:id
```

### Atualiza dados de funcionário

```
PUT /employee/:id
```

Body

```json
{
    "name": "Foo Bar",
    "email": "foo@bar.com",
    "department": "Mobile"
}
```

### Remove um funcionário

```
DELETE /employee/:id
```

## Testes

Para execução dos testes de API, execute:


```
python manage.py test
```
