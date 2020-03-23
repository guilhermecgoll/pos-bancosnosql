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
> db.italians.find({$where : "(this.cat && this.cat.name && this.cat.age) || (this.dog && this.dog.name && this.dog.age)"}, {cat : 1, dog : 1, "_id" : 0})   
{ "cat" : { "name" : "Gianni", "age" : 11 } }
{ "cat" : { "name" : "Andrea", "age" : 4 } }
{ "cat" : { "name" : "Davide", "age" : 15 }, "dog" : { "name" : "Alessandro", "age" : 13 } }
{ "cat" : { "name" : "Pasquale", "age" : 1 } }
{ "dog" : { "name" : "Davide", "age" : 8 } }
{ "dog" : { "name" : "Raffaele", "age" : 4 } }
{ "cat" : { "name" : "Angela", "age" : 2 } }
{ "cat" : { "name" : "Enzo ", "age" : 1 }, "dog" : { "name" : "Daniela", "age" : 8 } }
{ "dog" : { "name" : "Enzo ", "age" : 12 } }
{ "cat" : { "name" : "Alex", "age" : 17 } }
{ "cat" : { "name" : "Lucia", "age" : 16 }, "dog" : { "name" : "Giorgio", "age" : 5 } }
{ "cat" : { "name" : "Massimo", "age" : 14 }, "dog" : { "name" : "Ilaria", "age" : 10 } }
{ "cat" : { "name" : "Marco", "age" : 6 }, "dog" : { "name" : "Alessio", "age" : 0 } }
{ "cat" : { "name" : "Lorenzo", "age" : 15 } }
{ "cat" : { "name" : "Angelo", "age" : 12 }, "dog" : { "name" : "Daniela", "age" : 0 } }
{ "dog" : { "name" : "Silvia", "age" : 10 } }
{ "cat" : { "name" : "Davide", "age" : 1 } }
{ "cat" : { "name" : "Alessio", "age" : 12 } }
{ "cat" : { "name" : "Massimo", "age" : 2 }, "dog" : { "name" : "Emanuela", "age" : 13 } }
{ "dog" : { "name" : "Valeira", "age" : 5 } }
Type "it" for more
```

### 12. Quais são as 5 pessoas mais velhas com sobrenome Rossi?

```sh
> db.italians.find({surname: "Rossi"}, {firstname : 1, surname : 1, age : 1}).limit(5).sort({age  : -1})
{ "_id" : ObjectId("5e7215ef9e92f0d468e01efc"), "firstname" : "Sonia", "surname" : "Rossi", "age" : 78 }   
{ "_id" : ObjectId("5e7215f69e92f0d468e0288a"), "firstname" : "Sara", "surname" : "Rossi", "age" : 76 }    
{ "_id" : ObjectId("5e7215e79e92f0d468e013ae"), "firstname" : "Sergio", "surname" : "Rossi", "age" : 75 }  
{ "_id" : ObjectId("5e7215fc9e92f0d468e030dc"), "firstname" : "Gabiele", "surname" : "Rossi", "age" : 75 } 
{ "_id" : ObjectId("5e7215f09e92f0d468e020d5"), "firstname" : "Cristian", "surname" : "Rossi", "age" : 74 }
```

### 13. Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano

```sh
> let italiano = {firstname : "Vito", surname : "Corleone", username : "thegodfather", age : 56, email: "vito.corleone@gmail.com", bloodType : "AB+", id_num : 895666244555, registerDate : new Date(), ticketNumber : 10001, jobs : [ "Tráfico", "Máfia"], favFruits : ["Uva", "Laranja"], movies : [ { title: "The Godfather", rating : 4.12}, {title : "The Godfather Part II", rating : 4.06 }], lion : {name : "Simba", age : 7}}
> db.italians.insert(italiano)  
WriteResult({ "nInserted" : 1 })
```

### 14. Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.

```sh
> db.italians.find(italiano)
{ "_id" : ObjectId("5e7385afa6b904a95b7cce11"), "firstname" : "Vito", "surname" : "Corleone", "username" : "thegodfather", "age" : 56, "email" : "vito.corleone@gmail.com", "bloodType" : "AB+", "id_num" : 895666244555, "registerDate" : ISODate("2020-03-19T14:46:05.240Z"), "ticketNumber" : 10001, "jobs" : [ "Tráfico", "Máfia" ], "favFruits" : [ "Uva", "Laranja" ], "movies" : [ { "title" : "The Godfather", "rating" : 4.12 }, { "title" : "The Godfather Part II", "rating" : 4.06 } ], "lion" : { "name" : "Simba", "age" : 7 } }
> db.italians.remove({"_id" : ObjectId("5e7385afa6b904a95b7cce11")})      
WriteResult({ "nRemoved" : 1 })
```

### 15. Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.

```sh
> db.italians.update({}, {$inc : {age : 1}}, {multi: true})
WriteResult({ "nMatched" : 10000, "nUpserted" : 0, "nModified" : 10000 })
```

### 16. O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.

```sh
> db.italians.remove({$where : "this.age == 66 && this.cat"})
WriteResult({ "nRemoved" : 79 })
```

### 17. Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.

```sh
> db.italians.aggregate([{ $match : { mother : { $exists : 1}}},
{'$project': {
        "firstname": 1,
        "mother": 1,
        "isEqual": { "$cmp": ["$firstname","$mother.firstname"]}
        }},
{'$match': {"isEqual": 0}}])
{ "firstname" : "Nicola", "mother" : { "firstname" : "Nicola", "surname" : "Bellini", "age" : 32 }, "isEqual" : 0 }       
{ "firstname" : "Emanuela", "mother" : { "firstname" : "Emanuela", "surname" : "Martinelli", "age" : 85 }, "isEqual" : 0 }
{ "firstname" : "Lucia", "mother" : { "firstname" : "Lucia", "surname" : "Costa", "age" : 39 }, "isEqual" : 0 }
{ "firstname" : "Roberto", "mother" : { "firstname" : "Roberto", "surname" : "Battaglia", "age" : 71 }, "isEqual" : 0 }   
{ "firstname" : "Teresa", "mother" : { "firstname" : "Teresa", "surname" : "Costatini", "age" : 72 }, "isEqual" : 0 }
{ "firstname" : "Antonella", "mother" : { "firstname" : "Antonella", "surname" : "Marino", "age" : 71 }, "isEqual" : 0 }
{ "firstname" : "Raffaele", "mother" : { "firstname" : "Raffaele", "surname" : "Benedetti", "age" : 98 }, "isEqual" : 0 }
```

### 18. Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome


```sh
> db.italians.aggregate([{$group : { _id : {firstname: "$firstname"}}}, {$sort : {_id : 1}}])
{ "_id" : { "firstname" : "Alberto" } }   
{ "_id" : { "firstname" : "Alessandra" } }
{ "_id" : { "firstname" : "Alessandro" } }
{ "_id" : { "firstname" : "Alessia" } }   
{ "_id" : { "firstname" : "Alessio" } }   
{ "_id" : { "firstname" : "Alex" } }      
{ "_id" : { "firstname" : "Andrea" } }    
{ "_id" : { "firstname" : "Angela" } }    
{ "_id" : { "firstname" : "Angelo" } }    
{ "_id" : { "firstname" : "Anna" } }      
{ "_id" : { "firstname" : "Antonella" } } 
{ "_id" : { "firstname" : "Antonio" } }
{ "_id" : { "firstname" : "Barbara" } }
{ "_id" : { "firstname" : "Carlo" } }
{ "_id" : { "firstname" : "Chiara" } }
{ "_id" : { "firstname" : "Cinzia" } }
{ "_id" : { "firstname" : "Claudia" } }
{ "_id" : { "firstname" : "Claudio" } }
{ "_id" : { "firstname" : "Cristian" } }
{ "_id" : { "firstname" : "Cristina" } }
Type "it" for more
```

### 19. Agora faça a mesma lista do item acima, considerando nome completo.

```sh
> db.italians.aggregate([{$group : { _id : {firstname: "$firstname", surname: "$surname"}}}, {$sort : {_id : 1}}])
{ "_id" : { "firstname" : "Alberto", "surname" : "Amato" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Barone" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Basile" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Battaglia" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Bellini" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Benedetti" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Bernardi" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Bianchi" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Bianco" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Bruno" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Caputo" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Carbone" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Caruso" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Cattaneo" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Conte" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Conti" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Costa" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Costatini" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "Damico" } }
{ "_id" : { "firstname" : "Alberto", "surname" : "De Angelis" } }
Type "it" for more
```

### 20. Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.

```sh
> db.italians.find({$where : "(this.cat || this.dog) && this.age > 20 && this.age < 60 && (this.favFruits.includes('Maçã') || this.favFruits.includes('Banana'))"}, {_id: 0, firstname: 1, favFruits : 1, dog: 1, cat : 1}).limit(10)
{ "firstname" : "Elena", "favFruits" : [ "Pêssego", "Banana" ], "cat" : { "name" : "Alex", "age" : 17 } }
{ "firstname" : "Sergio", "favFruits" : [ "Melancia", "Goiaba", "Banana" ], "dog" : { "name" : "Valeira", "age" : 5 } }
{ "firstname" : "Manuela", "favFruits" : [ "Tangerina", "Maçã", "Pêssego" ], "cat" : { "name" : "Luca", "age" : 13 } }
{ "firstname" : "Simone", "favFruits" : [ "Maçã" ], "dog" : { "name" : "Lorenzo", "age" : 2 } }
{ "firstname" : "Antonio", "favFruits" : [ "Maçã" ], "cat" : { "name" : "Serena", "age" : 12 } }
{ "firstname" : "Giusy", "favFruits" : [ "Kiwi", "Pêssego", "Banana" ], "cat" : { "name" : "Alessandro", "age" : 12 } }
{ "firstname" : "Paola", "favFruits" : [ "Banana", "Banana" ], "cat" : { "name" : "Mattia", "age" : 9 } }
{ "firstname" : "Claudia", "favFruits" : [ "Banana" ], "cat" : { "name" : "Massimiliano", "age" : 8 }, "dog" : { "name" : "Raffaele", "age" : 6 } }
{ "firstname" : "Veronica", "favFruits" : [ "Banana", "Banana" ], "cat" : { "name" : "Lucia", "age" : 16 } }
{ "firstname" : "Giovanna", "favFruits" : [ "Maçã", "Kiwi", "Uva" ], "cat" : { "name" : "Paola", "age" : 17 }, "dog" : { "name" : "Dario", "age" : 17 } }
```

## Exercício 3 - Stockbrokers

### 1. Liste as ações com profit acima de 0.5 (limite a 10 o resultado)

```sh
> db.stocks.find({"Profit Margin" : {$gt : 0.5}}, {"Ticker" : 1, "Profit Margin" : 1}).limit(10)
{ "_id" : ObjectId("52853800bb1177ca391c180f"), "Ticker" : "AB", "Profit Margin" : 0.896 }
{ "_id" : ObjectId("52853801bb1177ca391c1895"), "Ticker" : "AGNC", "Profit Margin" : 0.972 }
{ "_id" : ObjectId("52853801bb1177ca391c1950"), "Ticker" : "ARCC", "Profit Margin" : 0.654 }
{ "_id" : ObjectId("52853801bb1177ca391c195a"), "Ticker" : "ARI", "Profit Margin" : 0.576 }
{ "_id" : ObjectId("52853801bb1177ca391c1968"), "Ticker" : "ARR", "Profit Margin" : 0.848 }
{ "_id" : ObjectId("52853801bb1177ca391c1998"), "Ticker" : "ATHL", "Profit Margin" : 0.732 }
{ "_id" : ObjectId("52853801bb1177ca391c19f6"), "Ticker" : "AYR", "Profit Margin" : 0.548 }
{ "_id" : ObjectId("52853801bb1177ca391c1a97"), "Ticker" : "BK", "Profit Margin" : 0.63 }
{ "_id" : ObjectId("52853801bb1177ca391c1abd"), "Ticker" : "BLX", "Profit Margin" : 0.588 }
{ "_id" : ObjectId("52853801bb1177ca391c1af0"), "Ticker" : "BPO", "Profit Margin" : 0.503 }
```

### 2. Liste as ações com perdas (limite a 10 novamente)

```sh
> db.stocks.find({"Profit Margin" : {$lt : 0}}, {"Ticker" : 1, "Profit Margin" : 1}).limit(10)  
{ "_id" : ObjectId("52853800bb1177ca391c1806"), "Ticker" : "AAOI", "Profit Margin" : -0.023 }
{ "_id" : ObjectId("52853800bb1177ca391c180c"), "Ticker" : "AAV", "Profit Margin" : -0.232 }
{ "_id" : ObjectId("52853800bb1177ca391c1815"), "Ticker" : "ABCD", "Profit Margin" : -0.645 }
{ "_id" : ObjectId("52853800bb1177ca391c1817"), "Ticker" : "ABFS", "Profit Margin" : -0.005 }
{ "_id" : ObjectId("52853800bb1177ca391c181b"), "Ticker" : "ABMC", "Profit Margin" : -0.0966 }
{ "_id" : ObjectId("52853800bb1177ca391c1821"), "Ticker" : "ABX", "Profit Margin" : -0.769 }
{ "_id" : ObjectId("52853800bb1177ca391c1826"), "Ticker" : "ACCL", "Profit Margin" : -0.014 }
{ "_id" : ObjectId("52853800bb1177ca391c182b"), "Ticker" : "ACFC", "Profit Margin" : -0.18 }
{ "_id" : ObjectId("52853800bb1177ca391c182f"), "Ticker" : "ACH", "Profit Margin" : -0.051 }
{ "_id" : ObjectId("52853800bb1177ca391c1832"), "Ticker" : "ACI", "Profit Margin" : -0.173 }
```

### 3. Liste as 10 ações mais rentáveis

```sh
> db.stocks.find({}, {"Ticker" : 1, "Profit Margin" : 1}).sort({"Profit Margin" : -1}).limit(10)
{ "_id" : ObjectId("52853801bb1177ca391c1af3"), "Ticker" : "BPT", "Profit Margin" : 0.994 }
{ "_id" : ObjectId("52853802bb1177ca391c1b69"), "Ticker" : "CACB", "Profit Margin" : 0.994 }
{ "_id" : ObjectId("5285380bbb1177ca391c2c3c"), "Ticker" : "ROYT", "Profit Margin" : 0.99 }
{ "_id" : ObjectId("52853808bb1177ca391c281b"), "Ticker" : "NDRO", "Profit Margin" : 0.986 }
{ "_id" : ObjectId("5285380fbb1177ca391c318e"), "Ticker" : "WHZ", "Profit Margin" : 0.982 }
{ "_id" : ObjectId("52853808bb1177ca391c27bd"), "Ticker" : "MVO", "Profit Margin" : 0.976 }
{ "_id" : ObjectId("52853801bb1177ca391c1895"), "Ticker" : "AGNC", "Profit Margin" : 0.972 }
{ "_id" : ObjectId("5285380ebb1177ca391c3101"), "Ticker" : "VOC", "Profit Margin" : 0.971 }
{ "_id" : ObjectId("52853807bb1177ca391c279a"), "Ticker" : "MTR", "Profit Margin" : 0.97 }
{ "_id" : ObjectId("52853809bb1177ca391c2946"), "Ticker" : "OLP", "Profit Margin" : 0.97 }
```

### 4. Qual foi o setor mais rentável?

```sh
db.stocks.aggregate([{$group : 
{ _id : {"Sector": "$Sector"}, 
total : { $sum : "$Profit Margin"}}}, 
{$sort : {total : -1}}, {$limit : 1}])
```
### 5. Ordene as ações pelo profit e usando um cursor, liste as ações.

```sh
> var cursor = db.stocks.find().sort({"Profit Margin" : -1})
> cursor.forEach(function(x) {print (x.Ticker + " -> " + x["Profit Margin"]);})
```

### 6. Renomeie o campo “Profit Margin” para apenas “profit”.

```sh
> db.stocks.updateMany({}, { $rename : {"Profit Margin" : "profit"}})
```

### 7. Agora liste apenas a empresa e seu respectivo resultado

```sh
> db.stocks.find({}, {"_id" : 0, Company : 1, profit : 1})
{ "Company" : "iShares MSCI AC Asia Information Tech" }
{ "Company" : "WCM/BNY Mellon Focused Growth ADR ETF" }
{ "Company" : "Alcoa, Inc.", "profit" : 0.013 }
{ "Company" : "Agilent Technologies Inc.", "profit" : 0.137 }
{ "Company" : "Altisource Asset Management Corporation" }
{ "Company" : "Atlantic American Corp.", "profit" : 0.056 }
{ "Company" : "Applied Optoelectronics, Inc.", "profit" : -0.023 }
{ "Company" : "Aaron's, Inc.", "profit" : 0.06 }
{ "Company" : "Advance Auto Parts Inc.", "profit" : 0.063 }
{ "Company" : "Apple Inc.", "profit" : 0.217 }
{ "Company" : "AAON Inc.", "profit" : 0.105 }
{ "Company" : "American Assets Trust, Inc.", "profit" : 0.155 }
{ "Company" : "Almaden Minerals Ltd." }
{ "Company" : "Advantage Oil & Gas Ltd.", "profit" : -0.232 }
{ "Company" : "iShares MSCI All Country Asia ex Jpn Idx" }
{ "Company" : "Atlas Air Worldwide Holdings Inc.", "profit" : 0.071 }
{ "Company" : "AllianceBernstein Holding L.P.", "profit" : 0.896 }
{ "Company" : "Abaxis Inc.", "profit" : 0.1 }
{ "Company" : "ABB Ltd.", "profit" : 0.069 }
{ "Company" : "AbbVie Inc.", "profit" : 0.24 }
Type "it" for more
```

### 8. Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?

```sh
> db.stocks.find({}).sort({"Relative Strength Index (14)" : -1}).limit(3)
```

### 9. Liste as ações agrupadas por setor

```sh
> db.stocks.aggregate([{$group : { _id : { "Sector" : "$Sector"}}}])
{ "_id" : { "Sector" : "Financial" } }
{ "_id" : { "Sector" : "Technology" } }
{ "_id" : { "Sector" : "Healthcare" } }
{ "_id" : { "Sector" : "Consumer Goods" } }
{ "_id" : { "Sector" : "Industrial Goods" } }
{ "_id" : { "Sector" : "Basic Materials" } }
{ "_id" : { "Sector" : "Services" } }
{ "_id" : { "Sector" : "Utilities" } }
{ "_id" : { "Sector" : "Conglomerates" } }
```

## Exercício 3 – Fraude na Enron!

Obs: o comando utilizado para importar o dataset foi:
```sh
mongoimport --db enron --collection enron --file enron.json
```

### 1. Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?

```sh
> db.enron.aggregate([{$group : {_id : {"Sender" : "$sender" }}}])
--ou
> db.enron.distinct('sender')
```

Para contar os registros:
```sh
> db.enron.distinct('sender').length 
2200
```

### 2. Contabilize quantos e-mails tem a palavra “fraud”

```sh
> db.enron.count({ $where : "this.text.includes('fraud')"})
23
```
