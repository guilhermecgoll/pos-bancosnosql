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

```sh
hbase(main):012:0> import java.util.Date
=> [Java::JavaUtil::Date]
hbase(main):013:0> put 'italians', '11', 'personal-data:name', 'Vito Corleoni'
Took 0.5445 seconds
hbase(main):014:0> put 'italians', '11', 'personal-data:city', 'Sicilia'
Took 0.0033 seconds
hbase(main):015:0> put 'italians', '11', 'personal-data:birthdate', Date.new(-1826683252000)
Took 0.0041 seconds
hbase(main):016:0> put 'italians', '11', 'professional-data:role', 'Gangster'
Took 0.0063 seconds
hbase(main):017:0> put 'italians', '11', 'professional-data:years-employment', '27'
Took 0.0050 seconds
hbase(main):018:0> put 'italians', '12', 'personal-data:name', 'Eros Ramazzotti'
Took 0.0090 seconds
hbase(main):019:0> put 'italians', '12', 'personal-data:city', 'Rome'
Took 0.0137 seconds
hbase(main):021:0> put 'italians', '12', 'personal-data:birthdate', Date.new(-195004800)
Took 0.0033 seconds
hbase(main):022:0> put 'italians', '12', 'professional-data:role', 'Singer'
Took 0.0040 seconds
hbase(main):023:0> put 'italians', '12', 'professional-data:years-employment', '38'
Took 0.0042 seconds
```

### 2. Adicione o controle de 5 versões na tabela de dados pessoais.

```sh
hbase(main):029:0> alter 'italians',  NAME => 'personal-data',  VERSIONS => '5'
Updating all regions with the new schema...
1/1 regions updated.
Done.
Took 1.8511 seconds
```

### 3. Faça 5 alterações em um dos italianos;

```sh
hbase(main):037:0> put 'italians', '12', 'personal-data:name', 'Eros Luciano Ramazzotti'
Took 0.0034 seconds
hbase(main):038:0> put 'italians', '12', 'personal-data:name', 'Eros Luciano Walter Ramazzotti'
Took 0.0042 seconds
hbase(main):039:0> put 'italians', '12', 'personal-data:name', 'Eros Luciano Walter Ramazzotti Molina'
Took 0.0083 seconds
hbase(main):040:0> put 'italians', '12', 'personal-data:name', 'Eros Ramazzotti'
Took 0.0052 seconds
```

### 4. Com o operador get, verifique como o HBase armazenou o histórico.

```sh
hbase(main):041:0> get 'italians', '12', {COLUMN => 'personal-data:name', VERSIONS => 5}
COLUMN                                      CELL
 personal-data:name                         timestamp=1584701036692, value=Eros Ramazzotti
 personal-data:name                         timestamp=1584701027358, value=Eros Luciano Walter Ramazzotti Molina
 personal-data:name                         timestamp=1584701019953, value=Eros Luciano Walter Ramazzotti
 personal-data:name                         timestamp=1584701011748, value=Eros Luciano Ramazzotti
 personal-data:name                         timestamp=1584699726708, value=Eros Ramazzotti
1 row(s)
Took 0.0217 seconds
```

### 5. Utilize o scan para mostrar apenas o nome e profissão dos italianos.

```sh
hbase(main):045:0> scan 'italians', {COLUMNS => ['personal-data:name','professional-data:role'] }
ROW                                         COLUMN+CELL
 1                                          column=personal-data:name, timestamp=1584695817993, value=Paolo Sorrentino
 1                                          column=professional-data:role, timestamp=1584695818042, value=Gestao Comercial
 10                                         column=personal-data:name, timestamp=1584695818356, value=Giovanna Caputo
 10                                         column=professional-data:role, timestamp=1584695818375, value=Comunicacao Institucional
 11                                         column=personal-data:name, timestamp=1584699605520, value=Vito Corleoni
 11                                         column=professional-data:role, timestamp=1584699605678, value=Gangster
 12                                         column=personal-data:name, timestamp=1584701036692, value=Eros Ramazzotti
 12                                         column=professional-data:role, timestamp=1584700112052, value=Singer
 2                                          column=personal-data:name, timestamp=1584695818055, value=Domenico Barbieri
 2                                          column=professional-data:role, timestamp=1584695818069, value=Psicopedagogia
 3                                          column=personal-data:name, timestamp=1584695818104, value=Maria Parisi
 3                                          column=professional-data:role, timestamp=1584695818119, value=Optometria
 4                                          column=personal-data:name, timestamp=1584695818130, value=Silvia Gallo
 4                                          column=professional-data:role, timestamp=1584695818146, value=Engenharia Industrial Madeireira
 5                                          column=personal-data:name, timestamp=1584695818174, value=Rosa Donati
 5                                          column=professional-data:role, timestamp=1584695818195, value=Mecatronica Industrial
 6                                          column=personal-data:name, timestamp=1584695818209, value=Simone Lombardo
 6                                          column=professional-data:role, timestamp=1584695818223, value=Biotecnologia e Bioquimica
 7                                          column=personal-data:name, timestamp=1584695818233, value=Barbara Ferretti
 7                                          column=professional-data:role, timestamp=1584695818275, value=Libras
 8                                          column=personal-data:name, timestamp=1584695818291, value=Simone Ferrara
 8                                          column=professional-data:role, timestamp=1584695818305, value=Engenharia de Minas
 9                                          column=personal-data:name, timestamp=1584695818324, value=Vincenzo Giordano
 9                                          column=professional-data:role, timestamp=1584695818341, value=Marketing
12 row(s)
Took 0.0652 seconds
```

### 6. Apague os italianos com row id ímpar

```sh
hbase(main):046:0> deleteall 'italians', '1'
Took 0.0139 seconds
hbase(main):047:0> deleteall 'italians', '3'
Took 0.0031 seconds
hbase(main):048:0> deleteall 'italians', '5'
Took 0.0087 seconds
hbase(main):049:0> deleteall 'italians', '7'
Took 0.0092 seconds
hbase(main):050:0> deleteall 'italians', '9'
Took 0.0040 seconds
hbase(main):051:0> deleteall 'italians', '11'
Took 0.0074 seconds
```

### 7. Crie um contador de idade 55 para o italiano de row id 5

```sh
hbase(main):056:0> incr 'italians', '55', 'personal-data:age', 55
COUNTER VALUE = 55
Took 0.0231 seconds
```

### 8. Incremente a idade do italiano em 1

```sh
hbase(main):064:0> incr 'italians', '5', 'personal-data:age', 1
COUNTER VALUE = 56
```