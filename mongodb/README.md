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
