# open-source-challenge
Teste técnico Desenvolver Júnior

## Motivação

O projeto foi desenvolvido utilizando Python juntamente com Django e o Django REST Framework para a criação das APIs. Para a busca da organização foi utilizado a api do [Github](https://docs.github.com/pt/rest) e para a codificação dos testes foi utilizado a biblioteca pytest.

## Requisitos

* Django

* Django REST Framework

* requests

* gunicorn

* psycopg2

* django-heroku

* pytest

Para instalar os requisitos é necessário estar na pasta que possui o arquivo Pipfile e rodar o seguinte comando:

 ```
 pipenv install
 ```

Para ativar o ambiente virtual é necessário rodar o seguinte comando:
 ```
 pipenv shell
 ```
 
## Banco de dados
 
Para o banco será necessário aplicar as migrações:
```
python manage.py migrate
```

## Rodando o servidor
 
Utilize o seguinte comando para ativar o servidor local:

```
python manage.py runserver
```

## APIs

Foi feito o deploy do projeto no Heroku e para acessar os endpoints da API será necessário acessar os endpoints pelo Heroku [vough-opensource](https://vough-opensource.herokuapp.com/api/)

A API permite apenas 2 tipos de requisição e elas são GET e DELETE. No GET temos a listagem de todas as organizações open source salvas no banco de dados e o detalhamento de uma única organização e caso essa organização não esteja no banco essa organização será adicionada no banco e o DELETE possui apenas a deleção de uma organização que esta salvo no banco de dados.

### GET

Na requisição GET a API pode receber um `login` para buscar uma organização em específico ou não receber parâmentro nenhum para retornar a lista de todas as organizações que foram pesquisadas utizliando a API ordenadas pelo `score` em ordem decrescente.

#### Listagem de organizações

O endpoint de listagem de organizações quando chamado retorna as organizações que estão salvas no banco de dados ordenadas pelo score em ordem decrescente. Retorna também status `200` caso possua pelo menos 1 organização no banco de dados e caso não tenha nenhuma organização no banco de dados retorna o status `404`. Para acessar esse endpoint é necessário acessar a seguinte url.

```
https://vough-opensource.herokuapp.com/api/orgs/
```

O formato do retorno caso tenha 1 ou mais organizações será:

```
[
  {
    "login": "string",
    "name": "string",
    "score": int
  },
  {
    "login": "string",
    "name": "string",
    "score": int
  },
  ...
]
```
#### Detalhes de uma organização

O endpoint de detalhe de organização recebe o `login` da organização no Github e inicialmente busca essa organização no banco de dados, caso a organização for encontrada no banco a API retornará o status `200` e os detalhes da organização, caso a organização não for encontrada no banco será realizada uma requisição para a API do Github buscando as informações da organização e se essa organização for encontrada os detalhes serão salvos no banco e a resposta será o status `200` e os detalhes da organização, mas se a organização não for encontrada pela API do Github será retornado o status `404`. Para acessar esse endpoint é necessário acessar a seguinte url.

```
https://vough-opensource.herokuapp.com/api/orgs/<login da organização>
```
O formato do retorno caso a organização seja encontrada:

```
{
    "login": "string",
    "name": "string",
    "score": int
}
```

### DELETE

Na requisição DELETE a API tem que receber um `login` para buscar uma organização e deleta-lá do banco de dados.

#### Deleção de organização

O endpoint de deleção de organização tem que receber o `login` da organização do Github, busca esse `login` no banco de dados, se encontrar a organização no banco de dados essa organização será deletada e retorna um status `204` e caso essa organização não for encontrada retorna um status `404`. Para acessar esse endpoint é necessário acessar a seguinte url:
```
https://vough-opensource.herokuapp.com/api/orgs/<login da organização>
```

## Documentação da API

Arquivo de descrição do swagger esta na pasta mas não consegui entender como fazer funcionar a execução da API pelo swagger.
