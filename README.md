# testeAnalistaDeDados

Este repositório armazena um pequeno projeto para uma entrevista de analise de dados.

A proposta é bem simples:
![image](https://github.com/tlsabara/testeAnalistaDeDados/assets/78706759/a03b389d-fcf3-4ece-8b3d-bfed859d699a)

### SOURCE DATA
Vou criar um script em python para mockar os dados.

### ETL
Com docker vou usar o apache airflow para orquestrar o job.

### TARGET DATA
Vou ter um schema para os dados coletados e outro para os dados analisados. *O que encaixa mais com os projetos de analise de dados que realizei*


## Executando o projeto

### PostgreSQL - Origem

### PostgreSQL - Destino

### Airflow

O Apache Airflow vai ser o nosso orquestrador no projeto.

1. acesse a pasta: `cd ./airflow`
2. Inicie a configuração dos bancos de dados: `docker compose down --volumes --rmi all`
3. Realize a limpeza dos containers criados: `docker compose down --volumes --remove-orphans`
4. Inicialize o docker compose: `docker compose up -d`

