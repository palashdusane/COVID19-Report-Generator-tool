#author: Palash Dusane (palashdusane@gmail.com)

import sqlite3
import datetime as dt

#Global Variables
current_date= int(dt.date.today().strftime("%d%m%y"))
connection = sqlite3.connect('masterdb.sqlite')
cur = connection.cursor()

def createtable_covid19India():
    '''create table covid19India in database masterdb'''
    cur.execute('''
        CREATE TABLE IF NOT EXISTS covid19India(
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        current_date INTEGER NOT NULL,
        state_ut VARCHAR(50),
        confirmed_cases INTEGER,
        cured_cases INTEGER,
        deaths INTEGER,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
        )

def insert_covid19India(state_ut,confirmed_cases,cured_cases,deaths):
    '''Insert web-scraped data into covid19India table'''
    deaths = str(deaths).replace("#","")
    if(confirmed_cases.strip()==""): confirmed_cases = '0'
    if(cured_cases.strip()==""): cured_cases = '0'
    if(deaths.strip()==""): deaths='0'
    cur.execute('''INSERT INTO covid19India(current_date,state_ut,confirmed_cases,cured_cases,deaths)
                VALUES (?,?,?,?,?)''', (current_date,state_ut,int(confirmed_cases),int(cured_cases),int(deaths)))
    
def checkdate_covid19India():
    '''It checks for today's data (by date), returns false if data is not already inserted into covid19India table '''
    cur.execute("SELECT * FROM covid19India WHERE covid19India.current_date=?",(current_date,))
    try:
        data_rows = cur.fetchall()
    except:
        data_rows = []
    if(len(data_rows) > 0):
        return True
    else:
        return False
    
def getdata_covid19India(today_date):
    '''get data from covid19India table by a particular date'''
    cur.execute('''SELECT state_ut,confirmed_cases,cured_cases,deaths FROM covid19India 
                WHERE covid19India.current_date = ?''',(today_date,))
    rows = cur.fetchall()
    return rows

def gettop5_covid19India(current_date):
    '''get 5 most affected state data'''
    cur.execute('''SELECT state_ut,confirmed_cases,cured_cases,deaths FROM covid19India 
                WHERE covid19India.current_date =? ORDER BY confirmed_cases DESC LIMIT 5''',(current_date,))
    five_rows = cur.fetchall()
    return five_rows

def getlast5_covid19India(current_date):
    '''get 5 least affected state data'''
    cur.execute('''SELECT state_ut,confirmed_cases,cured_cases,deaths FROM covid19India 
                WHERE covid19India.current_date =? ORDER BY confirmed_cases LIMIT 5''',(current_date,))
    five_rows = cur.fetchall()
    return five_rows
    
    
def database_commit():
    '''commit all inserted records'''
    connection.commit()

def close_database():
    '''close cursor and connection'''
    cur.close()
    connection.close()
    
