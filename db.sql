create table if not EXISTS produtos(
  id integer PRIMARY KEY AUTOINCREMENT not NULL,
  nome varchar(50) not NULL,
  preco integer not NULL,
  qtde integer not NULL
);

insert into produtos(nome, preco, qtde) VALUES ('Rubber ducky', 25000, 4);