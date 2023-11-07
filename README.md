# testeAnalistaDeDados

Este repositório armazena um pequeno projeto para uma entrevista de analise de dados.

A proposta é bem simples:
![image](_assets/image/tarefa.png)

- Realizar a migração dos dados entre SOURCE e TARGET
- Utilizar Docker no Projeto
- Python com alguma forma de agendamento
- Enviar um relatório sumarizando os itens.
  - Quantidade de pontos por usuário
  - Quantidade de pontos por empresa
  - 10 Usuários com mais pontos
  - Média de marcações

---
## Minha Solução
### Jujpyter - Faker - Mock Data
???

### PostgreSQL - Origem
???

### PostgreSQL - Destino
???

### Airflow
????

---
## Executando o projeto

### REQUISITOS:
 - Docker
 - Python (3.9+) 

### Arquivo: **projeto.py**

Este arquivo foi criado para facilitar a execução do projeto.

1. Configurar email  para receber os avisos:
   - O projeto precisa de um email apenas para receber os alertas e resultados dos processos de etl.
   - na raiz do projeto execute: `python projeto.py --configurar`
2. Rodando o projeto:
   - Para executar o projeto execute: `python projeto.py --iniciar`
   - Este comando irá criar os containers necessários para a execução.
   - Para acessar o airflow e ver o pipeline acesse [localhost:8080](http://localhost:8080).
   - Para acessar o banco de dados de ORIGEM:
   ```shell
   Servidor: localhost
   Porta: 10000
   Usuário: postgres
   Senha: senhasourcedb
   ```
   - Para acessar o banco de dados de DESTINO:
   ```shell
   Servidor: localhost
   Porta: 11000
   Usuário: postgres
   Senha: senhatargetdb
   ```
3. Parando o projeto:
   - Após avaliar o projeto execute: ``

---
## Considerações
???