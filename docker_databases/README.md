## BANCOS DE DADOS

Este arquivo docker compose cria 02 instancias de banco de dados Postgres SQL.

### Banco de dados de origem
O banco ja inicia com os dados contidos no script de `init.sql`.
- Conexão:
  - `username: postgres`
  - `password: senhasourcedb`
  - `server: localhost`
  - `database: postgres`

### Banco de dados de destino
Apenas uma instancia de vazia.
- Conexão:
  - `username: postgres`
  - `password: senhatargetdb`
  - `server: localhost`
  - `database: postgres`

---
ps: 
- São 50.000 linhas no banco de origem então a inicialização do container pode demorar uns 3-5 min.
- Caso consider o volume de 50k baixo, pode renomear o arquivo `init_src_500k.sql` para `init_src.sql`, que o container iniciará com 500K linhas(demora 10-15min na incialização)
