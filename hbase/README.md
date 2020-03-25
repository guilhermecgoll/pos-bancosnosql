# Aquecendo com alguns dados

## Agora, de dentro da imagem faça os sefuintes procedimentos:

### 1. Crie a tabela com 2 famílias de colunas:
a. personal-data
b. professional-data

```sh
hbase(main):004:0> create 'italians','personal-data','professional-data'
Created table italians
Took 0.7636 seconds
=> Hbase::Table - italians
```

### 2. Importe o arquivo via linha de comando

```sh
hbase shell /tmp/hbase/italians.txt
2020-03-20 09:16:56,741 WARN  [main] util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
...
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: http://hbase.apache.org/2.0/book.html#shell
Version 2.1.2, r1dfc418f77801fbfb59a125756891b9100c1fc6d, Sun Dec 30 21:45:09 PST 2018
Took 0.0016 seconds
```

## Agora execute as seguintes operações:

### 1. Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais;

### 2. Adicione o controle de 5 versões na tabela de dados pessoais.
### 3. Faça 5 alterações em um dos italianos;
### 4. Com o operador get, verifique como o HBase armazenou o histórico.
### 5. Utilize o scan para mostrar apenas o nome e profissão dos italianos.
### 6. Apague os italianos com row id ímpar
### 7. Crie um contador de idade 55 para o italiano de row id 5
### 8. Incremente a idade do italiano em 1