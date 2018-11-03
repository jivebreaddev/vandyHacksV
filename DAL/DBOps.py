import sqlalchemy
import pyodbc
import pandas as pd
import Models.Account as M
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

def retrieveAccount(username):
    sql = """
    select * from Account where username = '%s'
    """ % username
    record = pd.read_sql(sql, engine)
    returnValue = M.Account(record['FName'][0], record['LName'][0],
                            record['email'][0], record['phone'][0],
                            record['UserName'][0], record['pword'][0],
                            record['oAuth'][0]
                            )
    return returnValue

def insertAccount(Account):
    cursor = engine.raw_connection().cursor()
    cursor.execute("InsertAccount ?,?,?,?,?,?,?", Account.toParams())
    cursor.commit()

