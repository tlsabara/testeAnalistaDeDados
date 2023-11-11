"""Neste arquivo é realizada a migração dos dados

Para realziar a migração dos dados realizamos a conexão com o Banco de Origem,
criamos um dataframe e o enviamos ao banco de destino.
"""

import pandas as pd
from sqlalchemy import create_engine

url_db_source = "postgresql+pg8000://postgres:senhasourcedb@localhost:10000/sourcedb"
url_db_target = "postgresql+pg8000://postgres:senhatargetdb@localhost:11000/targetdb"

src_engine = create_engine(url_db_source)
target_engine = create_engine(url_db_target)

src_sql = "SELECT * FROM t_ponto"
pd.read_sql(src_sql, src_engine).to_sql("t_ponto_migration",target_engine, index=False )
