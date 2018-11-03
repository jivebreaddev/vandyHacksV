import sqlalchemy
import pyodbc
import pandas as pd
import Models as model
import urllib

params = urllib.parse.quote("DRIVER={ODBC Driver 13 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=vandyhacksv;Trusted_Connection=yes")
engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)

def Authenticate(username, password):
    sql = """select username, pword from Account where username = '%s' and pword = '%s' """ % (username, password)
    records = pd.read_sql(sql, engine)
    if(records.empty):
        return False
    else:
        return True
