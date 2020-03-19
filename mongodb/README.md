# MongoDB

Abaixo segue resposta dos exercícios do MongoDB.

## Exercício 1- Aquecendo com os pets

### 1. Adicione outro Peixe e um Hamster com nome Frodo

```sh
> db.pets.insert({name: "Frodo", species: "Peixe" })
WriteResult({ "nInserted" : 1 })
> db.pets.insert({name: "Frodo", species: "Hamster" })
WriteResult({ "nInserted" : 1 })
```

### 2. Faça uma contagem dos pets na coleção

```sh
> db.pets.count()
8
```

### 3. Retorne apenas um elemento o método prático possível

```sh
> db.pets.findOne()
{
        "_id" : ObjectId("5e717635efd76bd7dd067eb6"),
        "name" : "Mike",
        "species" : "Hamster"
}
```

### 4. Identifique o ID para o Gato Kilha.

```sh
> db.pets.find({name: "Kilha", species: "Gato"}, {"_id" : 1})
{ "_id" : ObjectId("5e717635efd76bd7dd067eb8") }
```

### 5. Faça uma busca pelo ID e traga o Hamster Mike

```sh
> db.pets.findOne({"_id" : ObjectId("5e717635efd76bd7dd067eb6")})
{
        "_id" : ObjectId("5e717635efd76bd7dd067eb6"),
        "name" : "Mike",
        "species" : "Hamster"
}
```

### 6. Use o find para trazer todos os Hamsters

```sh
> db.pets.find({species: "Hamster"})
{ "_id" : ObjectId("5e717635efd76bd7dd067eb6"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5e717817efd76bd7dd067ebd"), "name" : "Frodo", "species" : "Hamster" }
```

### 7. Use o find para listar todos os pets com nome Mike

```sh
> db.pets.find({name:"Mike"})
{ "_id" : ObjectId("5e717635efd76bd7dd067eb6"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5e717635efd76bd7dd067eb9"), "name" : "Mike", "species" : "Cachorro" }
```

### 8. Liste apenas o documento que é um Cachorro chamado Mike

```sh
> db.pets.findOne({name:"Mike", species:"Cachorro"})
{
        "_id" : ObjectId("5e717635efd76bd7dd067eb9"),
        "name" : "Mike",
        "species" : "Cachorro"
}
```

## Exercício 2 – Mama mia!

### 1. Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade.

```sh
> db.italians.count({age: 99})
0
```
### 2. Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)

```sh
> db.italians.count({age : {"$gt" : 65}})
1695
```

### 3. Identifique todos os jovens (pessoas entre 12 a 18 anos).

```sh
> db.italians.count({age: {"$gte": 12, "$lte" : 18}})
916
```

Obs: o enunciado pede para identificar, mas por serem muitos registros, apenas listei a quantidade.

### 4. Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois

```sh
> db.italians.count({cat : {"$exists" : true}})
6002
> db.italians.count({dog : {"$exists" : true}})
3890
> db.italians.count({"$and" : [{dog: null}, {cat: null}]})
2472
```

### 5. Liste/Conte todas as pessoas acima de 60 anos que tenham gato

```sh
> db.italians.count({"$and" : [{age : {"$gt" : 60}}, {cat : {"$exists" : true}}]}) 
1397
```

### 6. Liste/Conte todos os jovens com cachorro

```sh
> db.italians.count({"$and" : [{age: {"$gte": 12, "$lte" : 18}}, {dog : {"$exists" : true}}]})
357
```

### 7. Utilizando o $where, liste todas as pessoas que tem gato e cachorro

```sh
> db.italians.count({ $where : "this.dog && this.cat"})
2364
```

Obs: o enunciado pede para listar, mas por serem muitos registros, apenas apresentei a quantidade.

### 8. Liste todas as pessoas mais novas que seus respectivos gatos.

```sh
> db.italians.count({$where : "this.cat && this.age < this.cat.age"})
678
```

### 9. Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)

```sh
> db.italians.count({$where : "(this.cat && this.firstname == this.cat.name) || (this.dog && this.firstname == this.dog.name)"})
85
```

### 10. Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo

```sh
> db.italians.find({$where : "this.bloodType.includes('-')"}, {"_id" : 0, "firstname" : 1, "surname" : 1})
{ "firstname" : "Gianni", "surname" : "D’Amico" }
{ "firstname" : "Anna", "surname" : "Moretti" }
{ "firstname" : "Cristian", "surname" : "Parisi" }
{ "firstname" : "Domenico", "surname" : "Rizzi" }
{ "firstname" : "Daniele", "surname" : "Fontana" }
{ "firstname" : "Riccardo", "surname" : "Villa" }
{ "firstname" : "Alessandra", "surname" : "Vitale" }
{ "firstname" : "Antonio", "surname" : "D’Angelo" }
{ "firstname" : "Elena", "surname" : "D’Amico" }
{ "firstname" : "Stefano", "surname" : "Mancini" }
{ "firstname" : "Pietro", "surname" : "Negri" }
{ "firstname" : "Rita", "surname" : "Giuliani" }
{ "firstname" : "Gianni", "surname" : "Ricci" }
{ "firstname" : "Elisabetta", "surname" : "Sartori" }
{ "firstname" : "Nicola", "surname" : "Vitali" }
{ "firstname" : "Alessio", "surname" : "Ferrara" }
{ "firstname" : "Fabio", "surname" : "Russo" }
{ "firstname" : "Pietro", "surname" : "Fabbri" }
{ "firstname" : "Federico", "surname" : "Ferraro" }
{ "firstname" : "Manuela", "surname" : "Giuliani" }
Type "it" for more
```

### 11. Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId)

```sh
```

### 12. Quais são as 5 pessoas mais velhas com sobrenome Rossi?

```sh
```

### 13. Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano

```sh
```

### 14. Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.

```sh
```

### 15. Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.

```sh
```

### 16. O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.

```sh
```

### 17. Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.

```sh
```

### 18. Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome


```sh
```

### 19. Agora faça a mesma lista do item acima, considerando nome completo.

```sh
```

### 20. Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.

```sh
```

## Exercício 3 - Stockbrokers

### 1. Liste as ações com profit acima de 0.5 (limite a 10 o resultado)

```sh
```

### 2. Liste as ações com perdas (limite a 10 novamente)

```sh
```

### 3. Liste as 10 ações mais rentáveis

```sh
```

### 4. Qual foi o setor mais rentável?

```sh
```
### 5. Ordene as ações pelo profit e usando um cursor, liste as ações.

```sh
```

### 6. Renomeie o campo “Profit Margin” para apenas “profit”.

```sh
```

### 7. Agora liste apenas a empresa e seu respectivo resultado

```sh
```

### 8. Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?

```sh
```

### 9. Liste as ações agrupadas por setor

```sh
```

## Exercício 3 – Fraude na Enron!

### 1. Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?

```sh
```

### 2. Contabilize quantos e-mails tem a palavra “fraud”

```sh
```

