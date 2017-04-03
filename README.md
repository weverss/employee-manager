# Employee Manager

## Dependências

Este projeto foi desenvolvido utilizando Python 3.5. Para instalar as dependências necessárias listadas no arquivo requirements.txt, execute o comando abaixo:

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
Crie um superusuário para acesso ao painel administrativo:

```
python manage.py createsuperuser
```

## Inicialize o servidor built-in:
```
python manage.py runserver
```
Painel administrativo: http://localhost:8000/admin/
API de funcionários: http://localhost:8000/employee/

## Exemplos de Requisições

### Lista funcionários

```
GET http://localhost:8000/employee/
```
### Adiciona novo funcionário

```
POST http://localhost:8000/employee/
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
GET http://localhost:8000/employee/:id
```

### Atualiza dados de funcionário

```
PUT http://localhost:8000/employee/:id
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
DELETE http://localhost:8000/employee/:id
```

## Testes

Para execução dos testes de API, rode a linha de comando abaixo:


```
python manage.py test
```
