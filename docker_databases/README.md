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
ps: São 10.000 linhas então a inicialização do container pode demorar uns 3-5 min.