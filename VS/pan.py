import sqlalchemy
import pandas as pd
engine=sqlalchemy.create_engine("postgres://postgres:password@172.17.0.1:5432/pf")
eco=pd.read_sql_table("extractor_configs_old",engine)
print(eco)