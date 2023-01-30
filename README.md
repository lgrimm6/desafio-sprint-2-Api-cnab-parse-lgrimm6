# desafio-sprint-2-Api-cnab-parse-lgrimm6

A api consiste receber e parsear um arquivo de texto(CNAB) e salvar suas informações(transações financeiras) em uma base de dados

## Instalação

#### Para windows

    Crie um ambiente virtual com o comando: python -m venv/venv
    Inicie com o comando: venv/scripts/activate
    Dentro do ambiente virtual execute: pip install -r requirements.txt
    Execute as migrações do banco utilizando: python manage.py migrate
    Inicie o servidor com o comando : python manage.py runserver
        atente-se para a porta utilizada preferencialmente [:8000](http://127.0.0.1:8000/)

#### Para Linux

    Crie um ambiente virtual com o comando: python -m venv/venv
    Inicie com o comando: source venv/bin/activate
    Dentro do ambiente virtual execute: pip install -r requirements.txt
    Execute as migrações do banco utilizando: python manage.py migrate
    Inicie o servidor com o comando : python manage.py runserver
        atente-se para a porta utilizada preferencialmente [:8000](http://127.0.0.1:8000/)
