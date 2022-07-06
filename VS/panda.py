import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from pandasql import sqldf   #pip install pandasql

    
    # Create the engine to connect to the PostgreSQL database
engine = sqlalchemy.create_engine('postgresql://postgres:password@172.17.0.1:5432/pf')
                                 #(database://usename:password@host:port/databaseName )
     
    # Read data from SQL table
sql_data = pd.read_sql_table('extractor_configs_old',engine)
sql_write=sql_data.to_sql('extractor_configs_old',engine,index=False,if_exists='append')


# engine.execute("alter table sql_data ADD ajay VARCHAR(25)")
engine.execute("SELECT * FROM sql_data LIMIT 2")
# q = "SELECT * FROM sql_data LIMIT 2"
# sqldf(q)