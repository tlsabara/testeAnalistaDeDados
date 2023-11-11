"""Neste arquivo é realizada a migração dos dados (Executavel apenas pelo Airflow)

Para realziar a migração dos dados realizamos a conexão com o Banco de Origem,
criamos um dataframe e o enviamos ao banco de destino.
"""

def run_data_migration():
    import datetime
    import pandas as pd
    from sqlalchemy import create_engine

    url_db_source = "postgresql+pg8000://postgres:senhasourcedb@postgres_source_server:5432/sourcedb"
    url_db_target = "postgresql+pg8000://postgres:senhatargetdb@postgres_target_server:5432/targetdb"

    src_engine = create_engine(url_db_source)
    target_engine = create_engine(url_db_target)

    src_sql = "SELECT * FROM t_ponto"
    df = pd.read_sql(src_sql, src_engine)
    df["etl_date"] = datetime.now()
    df.to_sql("t_ponto_migration",target_engine, index=False )

if __name__ == '__main__':
    run_data_migration()
