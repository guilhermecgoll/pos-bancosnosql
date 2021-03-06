# Redis

Este projeto implementa um bingo, utilizando Python, como linguagem de programação, e o Redis, como banco de dados.

## Pré-requisitos

- Ter o python 3.7 ou superior instalado.
- Ter um servidor local do Redis em execução.

## 1 - Setup e configuração

### 1.1 Clonar o repositório

Clone o repositório em questão:

``git clone https://github.com/guilhermecgoll/pos-bancosnosql.git``

### 1.2 Baixar as dependências

Obs: os comandos abaixo deverão ser executados através da linha de comando.

- Navegue até o diretório ``redis``.
- Em seguida crie um diretório virtual, ative-o, e instale a dependência do ``redis``:

```sh
python -m venv .venv
.\.venv\Scripts\activate
pip install redis
```

## 2 - Executar o programa

Para executá-lo basta navegar até o diretório ``redis`` e digitar o comando abaixo:

```sh
python .\redinsgo.py
```

O resultado esperado após a execução deste comando é algo similar a este abaixo:

```sh
Encontrou um ganhador!
Após sortear 84 números, encontramos os seguintes ganhadores:
usuario32
```