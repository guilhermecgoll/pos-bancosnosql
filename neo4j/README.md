# 1

:play https://guides.neo4j.com/intro-neo4j-exercises/01.html

### 1.1

match(n) return n

### 1.2

CALL db.Schema()

### 1.3

match(p:Person) return p

### 1.4

match(m:Movie) return m

# 2

:play https://guides.neo4j.com/intro-neo4j-exercises/02.html

### 2.1

match(m:Movie {released:2003}) return m

### 2.2

Clicar no ícone 'Table' do painel de resultado.

### 2.3

CALL db.propertyKeys

### 2.4

match(m:Movie {released:2006}) return m.title

### 2.5

match(m:Movie) return m.title, m.released, m.tagline

### 2.6

match(m:Movie) return m.title as Titulo, m.released as Lançamento, m.tagline as `Sub-título`

# 3

:play https://guides.neo4j.com/intro-neo4j-exercises/03.html

### 3.1

call db.schema

### 3.2

match(p:Person)-[:WROTE]->(:Movie {title:'Speed Racer'})
return p

### 3.3

match(p:Person {name: 'Tom Hanks'})--(m:Movie) return m.title

### 3.4

match(p:Person {name: 'Tom Hanks'})-[r]-(m:Movie) return m.title, type(r)

### 3.5

match(p:Person {name: 'Tom Hanks'})-[r:ACTED_IN]-(m:Movie) return m.title, r.roles

# 4

:play https://guides.neo4j.com/intro-neo4j-exercises/04.html

### 4.1

match(p:Person)-[:ACTED_IN]->(m:Movie)
where p.name = 'Tom Cruise'
return m.title

### 4.2

match(p:Person)
where p.born >= 1970 AND p.born <= 1979
return p.name, p.born

### 4.3

match(p:Person)-[:ACTED_IN]->(m:Movie)
where p.born > 1960 and m.title = 'The Matrix'
return p.name, p.born

### 4.4

match(m)
where m:Movie and m.released = 2000
return m.title

### 4.5

match(p)-[rel]->(m)
where p:Person and m:Movie and type(rel) = 'WROTE'
return p.name, m.title

### 4.6

match(p:Person)
where not exists(p.born)
return p.name

### 4.7

match(p:Person)-[rel]->(m:Movie)
where exists(rel.rating)
return p.name, m.title, rel.rating

### 4.8

match(p:Person)-[:ACTED_IN]->(:Movie)
where p.name starts with('James')
return p.name

### 4.9

match(:Person)-[rel:REVIEWED]->(m:Movie)
where toLower(rel.summary) contains ('fun')
return m.title as Movie, rel.rating, rel.summary

### 4.10

match(p:Person)-[r:PRODUCED]->(m:Movie)
WHERE NOT((p)-[:DIRECTED]->(:Movie))
return p.name, m.title as Movie

### 4.11

match(a:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(d:Person)
where exists((d)-[:DIRECTED]->(m))
return a.name as ator, d.name as diretor, m.title as filme

### 4.12

match(m:Movie)
where m.released in [2000,2004,2008]
return m.title, m.released

### 4.13

match(:Person)-[r:ACTED_IN]->(m:Movie)
where m.title in (r.roles)
return m.title, r.roles

# 5

:play https://guides.neo4j.com/intro-neo4j-exercises/05.html

### 5.1

match(p1:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(p2:Person),
(p3:Person)-[:ACTED_IN]->(m)
where p1.name = 'Gene Hackman'
return m.title as Movie, p2.name as Director, collect(p### 3.name) as Atores

### 5.2

match(p1:Person)-[:FOLLOWS]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2

### 5.3

match(p1:Person)-[:FOLLOWS*3]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2

### 5.4

match(p1:Person)-[:FOLLOWS*1..2]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2

### 5.5

match(p1:Person)-[:FOLLOWS*]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2

### 5.6

match(p:Person)
where p.name starts with 'Tom'
optional match (p)-[:DIRECTED]->(m:Movie)
return p.name, m.title as Dirigiu

### 5.7

match(p:Person)-[:ACTED_IN]->(m:Movie)
return p.name as Ator, collect(m.title) as Filmes

### 5.8

match(a:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(b:Person)
where a.name = 'Tom Cruise'
return m.title as Filme, collect(b.name) as coadjuvantes

### 5.9

match(p:Person)-[:REVIEWED]->(m:Movie)
return m.title as Filme, count(p) as `Quantidade de Revisores`, collect(p.name) as Revisores

### 5.10

match(d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person)
return d.name as Diretor, count(a) as `Quantidade de atores com quem trabalhou`, collect(a.name) as Atores

### 5.11

match(p:Person)-[:ACTED_IN]->(m:Movie)
with p, count(p) as qtdFilmes, collect(m.title) as Filmes
where qtdFilmes = 5
return p.name as Ator, Filmes

### 5.12

match (m:Movie)
with m, size((:Person)-[:DIRECTED]->(m)) AS qtdDiretores
where qtdDiretores >= 2
optional match (p:Person)-[:REVIEWED]->(m)
return  m.title as Filme, p.name as Revisores

# 6

:play https://guides.neo4j.com/intro-neo4j-exercises/06.html

### 6.1

match(p:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 and m.released <= 1999
return m.title as filme, m.released as Lancamento, collect(p.name) as Atores

### 6.2

match(p:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 and m.released <= 1999
return m.released as Lancamento, collect(m.title) as Filmes, collect(p.name) as Atores

### 6.3

match(p:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 and m.released <= 1999
return m.released as Lancamento, collect(distinct m.title) as Filmes, collect(p.name) as Atores

### 6.4

match(p:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 and m.released <= 1999
return m.released as Lancamento, collect(distinct m.title) as Filmes, collect(p.name) as Atores order by Lancamento desc

### 6.5

match(m:Movie)<-[r:REVIEWED]-(:Person)
return m.title as Filme, r.rating as Nota
order by r.rating desc limit 5

### 6.6

match(p:Person)-[:ACTED_IN]->(m:Movie)
with p, count(p) as qtdAtuacoes, collect(m.title) as filmes
where qtdAtuacoes <= 3
return p.name, filmes

# 7

:play https://guides.neo4j.com/intro-neo4j-exercises/07.html

### 7.1

match(a:Person)-[:ACTED_IN]->(m:Movie), (m)<-[:PRODUCED]-(p:Person)
with m, collect(distinct a.name) as atores, collect(distinct p.name) as produtores
return distinct m.title as Filme, atores, produtores
order by size(atores)

### 7.2

match(a:Person)-[:ACTED_IN]->(m:Movie)
with a, collect(m) as filmes
where size(filmes) > 5
return a.name as Ator, filmes

### 7.3

match(a:Person)-[:ACTED_IN]->(m:Movie)
with a, collect(m) as filmes
where size(filmes) > 5
with a, filmes unwind filmes as filme
return a.name as Ator, filme.title

### 7.4

match(a:Person)-[:ACTED_IN]->(m:Movie)
where a.name = 'Tom Hanks'
return m.title as Filme, m.released, date().year - m.released as `Lançado há x anos atrás`, m.released - a.born as `Idade naquela época`

# 8

:play https://guides.neo4j.com/intro-neo4j-exercises/08.html

### 8.1

create(:Movie {title: 'Forrest Gump'})

### 8.2

match(m:Movie)
where m.title = 'Forrest Gump'
return m

### 8.3

create(:Person {name: 'Robin Wright'})

### 8.4

match(p:Person)
where p.name = 'Robin Wright'
return p

### 8.5

match(m:Movie)
where m.released < 2010
set m:OlderMovie
return distinct labels(m)

### 8.6

match(m:Movie)
where m:OlderMovie
return m

### 8.7

match(p:Person)
where p.name starts with 'Robin'
set p:Female
return distinct labels(p)

### 8.8

match(p:Female) return p

### 8.9

match(p:Female)
remove p:Female

### 8.10

call db.schema()

### 8.11

match(m:Movie)
where m.title = 'Forrest Gump'
set m.released = 1994, 
m.tagline = "Life is like a box of chocolates… you never know what you’re gonna get", 
m.lengthInMinutes = 142, 
m:OlderMovie
return m

### 8.12

match(m:OlderMovie)
where m.title = 'Forrest Gump'
return m.title, m.lengthInMinutes, m.tagline, m.released

### 8.13

match(p:Person)
where p.name = 'Robin Wright'
set p.born = 1966, p.birthPlace = "Dallas"

### 8.14

match(p:Person)
where p.name = 'Robin Wright'
return p

### 8.15

match(m:Movie)
where m.title = 'Forrest Gump'
set m.lengthInMinutes = null
return m

### 8.16

match(m:Movie)
where m.title = 'Forrest Gump'
return m

### 8.17

match(p:Person)
where p.name = 'Robin Wright'
set p.birthPlace = null

### 8.18

match(p:Person)
where p.name = 'Robin Wright'
return p

# 9

:play https://guides.neo4j.com/intro-neo4j-exercises/09.html

### 9.1

match(p:Person)
where p.name in ['Tom Hanks', 'Robin Wright', 'Gary Sinise']
match(m:Movie)
where m.title = 'Forrest Gump'
create (p)-[:ACTED_IN]->(m)

### 9.2

match(p:Person)
where p.name = 'Robert Zemeckis'
match(m:Movie)
where m.title = 'Forrest Gump'
create (p)-[:DIRECTED]->(m)

### 9.3

match(p1:Person)
where p1.name = 'Tom Hanks'
match(p2:Person)
where p2.name = 'Gary Sinise'
create (p1)-[:HELPED]->(p2)

### 9.4

match(p:Person)-[rel]-(m:Movie)
where m.title = 'Forrest Gump'
return p, rel, m

### 9.5

match(m:Movie)<-[r:ACTED_IN]-(p:Person)
where m.title = 'Forrest Gump'
set r.roles =
case p.name 
when 'Tom Hanks' then ['Forrest Gump']
when 'Robin Wright' then ['Jenny Curran']
when 'Gary Sinise' then ['Lieutenant Dan Taylor']
end

### 9.6

match(p1:Person)-[r:HELPED]-(p2:Person)
where p1.name = 'Tom Hanks' and p2.name = 'Gary Sinise'
set r.research = 'war history'
return p1, p2, r

### 9.7

call db.propertyKeys

### 9.8

call db.schema

### 9.9

match(p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title = 'Forrest Gump'
return p.name, r.roles

### 9.10

match(p1:Person)-[r:HELPED]-(p2:Person)
return p1, r, p2

### 9.11

match(p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title = 'Forrest Gump' and p.name = 'Gary Sinise'
set r.roles = ["Lt. Dan Taylor"]

### 9.12

match(p1:Person)-[r:HELPED]->(p2:Person)
where p1.name = 'Tom Hanks' and p2.name = 'Gary Sinise'
set r.research = null

### 9.13

match(p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title = 'Forrest Gump'
return p, r, m

# 10

:play https://guides.neo4j.com/intro-neo4j-exercises/10.html

### 10.1

match(p1:Person)-[r:HELPED]-(p2:Person)
delete r

### 10.2

match(p1:Person)-[r:HELPED]-(p2:Person)
return p1, r, p2

### 10.3

match(p1:Person)-[r]-(m:Movie)
where m.title = 'Forrest Gump'
return p1, r, m

### 10.4

match(m:Movie)
where m.title = 'Forrest Gump'
delete m

### 10.5

match(m:Movie)-[r]-(:Person)
where m.title = 'Forrest Gump'
delete r
delete m

### 10.6

match(m:Movie)
where m.title = 'Forrest Gump'
return m