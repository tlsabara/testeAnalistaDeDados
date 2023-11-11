"""Neste arquivo é realizada a analise solicitada

Aqui está apenas o código de execução, a explicação foi feita no notebook na pasta de scripts.
Arquivo: desenvolvimento_analise.ipynb
"""

import pandas as pd
from sqlalchemy import create_engine

url_db_source = "postgresql+pg8000://postgres:senhasourcedb@localhost:10000/sourcedb"
url_db_target = "postgresql+pg8000://postgres:senhatargetdb@localhost:11000/targetdb"

src_engine = create_engine(url_db_source)
target_engine = create_engine(url_db_target)

src_sql = "SELECT * FROM t_ponto"
df = pd.read_sql(src_sql, src_engine)

df_q1 = df.groupby(["username"]).count().id.reset_index()
df_q1.to_sql("q1__quantidade_apontamentos_ususario",target_engine, index=False)

df_q2 = df.groupby("company").count().id.reset_index()
df_q2.to_sql("q2__quantidade_apontamentos_empresa",target_engine, index=False )

df_q3 = df_q1.sort_values("id", ascending=False)[:10]
df_q3.to_sql("q3__top10_usuarios",target_engine, index=False )

df_q4 = df.copy()
df_q4["insert_date"] = df_q4["insert_date"].apply(lambda x: x.date())
df_q4 = df_q4.groupby('insert_date').count().id.reset_index()
df_q4.to_sql("q4__media_diaria",target_engine, index=False )

