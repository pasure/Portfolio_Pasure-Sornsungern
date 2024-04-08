import json
import requests
import pyodbc
import pandas as pd
from airflow.models import Variable
from sqlalchemy import create_engine

# [START extract_function]
def extract(**kwargs):    
    
    url_file_greentaxidata_2020 = Variable.get("url_greentaxidata_2020")
    url_file_greentaxidata_2021 = Variable.get("url_greentaxidata_2021")

    # fetching the request
    response_2020 = requests.get(url_file_greentaxidata_2020)
    response_2021 = requests.get(url_file_greentaxidata_2021)

    # convert the response to a pandas dataframe, then save as csv to the data    
    df2020 = pd.DataFrame(json.loads(response_2020.content))
    df2021 = pd.DataFrame(json.loads(response_2021.content))   
    df2020 = df2020.set_index("vendorid")
    df2021 = df2021.set_index("vendorid")

    # folder in our project directory   
    df2020.to_csv("data/taxi_2020.csv")
    df2021.to_csv("data/taxi_2021.csv")   
    print("Extract Done !! ")
# [END extract_function]

# [START transform_function]
def transform(**kwargs):
    dfall = pd.concat(
    map(pd.read_csv, ['data/taxi_2020.csv', 'data/taxi_2021.csv']))

    dfall = dfall.drop(columns=['store_and_fwd_flag'])
    dfall = dfall.drop_duplicates()
    dfall = dfall.set_index("vendorid")
    dfall.to_csv("data/taxi_2020-2021.csv")
    print("Transform Done !! ")    
# [END transform_function]

# [START savetojson_function]
def savetojson(**kwargs):
    df_csv = pd.read_csv("data/taxi_2020-2021.csv")
    df_csv.to_json("data/taxi_2020-2021.json")
    print("CSV to JSON Done !! ")
# [END savetojson_function]

# [START savetodb_function]
def savetodb(**kwargs):
    user = Variable.get("User")
    password = Variable.get("Password")
    host = Variable.get("Host")
    db= Variable.get("DB")
    TableName = Variable.get("TableName")
    SchemaName = Variable.get("SchemaName")

    # [Connect to Database (MSSQL SERVER)]
    Engine = create_engine(f'mssql+pyodbc://{user}:{password}@{host}/{db}?driver=ODBC+Driver+17+for+SQL+Server')   
    qurey5 = ("select * from taxi_2020_2021")
    print("Done !! ")
    dfTop5 = pd.read_sql(qurey5,Engine)
    print("Done !! ")
    print(dfTop5)

    # [Insert Data to Database (MSSQL SERVER)]
    df_csv = pd.read_csv("data/taxi_2020-2021.csv")
    df_csv.to_sql(TableName, con=Engine, schema=SchemaName, if_exists='replace', index=False)
    print("Save Data to Database Done !! ")
# [END savetodb_function]